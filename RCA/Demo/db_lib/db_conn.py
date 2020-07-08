import psycopg2
import xml_data_parser
class db_conn():

    def get_conn(self,user="user",password="password123",host="127.0.0.1",port="5432",database="des_db"):

        try:
                connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
                print ( connection.get_dsn_parameters(),"\n")

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)

        print(type(connection))
        return connection

    def close_conn(self,conn):
    #closing database connection.
        try:
            if(conn):
               conn.close()
            print("PostgreSQL connection is closed")
        except:
            print("Some issue in th DB closing")
    def loda_data_xml(self):
        pass
        print()



if __name__=="__main__":
    conn=db_conn().get_conn()
    cursor = conn.cursor()



    data_set=xml_data_parser.get_data()
    for i in data_set:
        sql_query="insert into "+str(i.get('suite'))+"(build_id,build_name,suite_name,tc_name,tc_id,run_status,start_time,end_time,output)values('"+\
                  str(i.get('build_id'))+"','"+str(i.get('build_id'))+"','"+str(i.get('suite'))+"','"+str(i.get('name'))+"','"+str(i.get('name'))+"','"+str(i.get('status'))+"','"+str(i.get('starttime'))+"','"+str(i.get('endtime'))+"','"+str(i.get('output'))+"');"
        try:
            cursor.execute(sql_query)
        except Exception as e:
            print(e)
        conn.commit()
        #break
    cursor.close()
    conn.close()










#############################################Garbage###################
# import psycopg2
# class db_conn():
#
#     def get_conn(self,user="user",password="password123",host="127.0.0.1",port="5432",database="des_db"):
#
#         try:
#                 connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
#                # self.cursor = connection.cursor()
#                 # Print PostgreSQL Connection properties
#                 print ( connection.get_dsn_parameters(),"\n")
#
#                 # Print PostgreSQL version
#                 # cursor.execute("SELECT version();")
#                 # record = cursor.fetchone()
#                 # print("You are connected to - ", record,"\n")
#
#                 #print(type(cursor))
#                 #return (cursor)
#         except (Exception, psycopg2.Error) as error :
#             print ("Error while connecting to PostgreSQL", error)
#         # finally:
#         #     #closing database connection.
#         #         if(connection):
#         #             cursor.close()
#         #             connection.close()
#         #             print("PostgreSQL connection is closed")
#
#
#         #cursor = connection.cursor()
#         # Print PostgreSQL Connection properties
#         print(connection.get_dsn_parameters(), "\n")
#
#         # Print PostgreSQL version
#         # cursor.execute("SELECT version();")
#         # record = cursor.fetchone()
#         # print("You are connected to - ", record,"\n")
#         print("$$$$$$$$$")
#         print(type(connection))
#         return connection
#
#
#
#
#     def close_conn(self,conn):
#     #closing database connection.
#         try:
#             if(conn):
#                conn.close()
#             print("PostgreSQL connection is closed")
#         except:
#             print("Some issue in th DB closing")