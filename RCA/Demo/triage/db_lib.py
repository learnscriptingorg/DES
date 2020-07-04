import psycopg2
class db_lib():

    def get_curr(self,user="user",password="password123",host="127.0.0.1",port="5432",database="des_db"):

        try:
                self.connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
                self.cursor = self.connection.cursor()
                # Print PostgreSQL Connection properties
                print ( self.connection.get_dsn_parameters(),"\n")

                # Print PostgreSQL version
                # cursor.execute("SELECT version();")
                # record = cursor.fetchone()
                # print("You are connected to - ", record,"\n")

                #print(type(cursor))
                #return (cursor)
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        # finally:
        #     #closing database connection.
        #         if(connection):
        #             cursor.close()
        #             connection.close()
        #             print("PostgreSQL connection is closed")


        cursor = self.connection.cursor()
        # Print PostgreSQL Connection properties
        print(self.connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        # cursor.execute("SELECT version();")
        # record = cursor.fetchone()
        # print("You are connected to - ", record,"\n")
        print("$$$$$$$$$")
        print(type(self.connection))
        return self.connection

    def close_conn(self):
    #closing database connection.
        try:
            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
        except:
            print("Some issue in th DB closing")