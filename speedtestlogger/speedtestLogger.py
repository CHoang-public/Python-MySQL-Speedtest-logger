import mysql.connector
import speedtest
import datetime


def runTest():
    
    print("")
    print("Initiating speedtest...")

    test = speedtest.Speedtest()
    
    testTime = datetime.datetime.now()
    
    down_speed = test.download()
    down_speed = int(down_speed / 1000000)
    print("Download speed:  " + str(down_speed) + " Mbps")
    
    up_speed = test.upload()
    up_speed = int(up_speed / 1000000)
    print("Upload speed:  " + str(up_speed) + " Mbps")
    print("")

    return (testTime, down_speed, up_speed)

def main():

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password" #replace with your password if it isn't set to password
  )

  print("Database connection: " + str(mydb))

  setDB = "USE speedtestDB;"
  
  resultTuple = runTest()
  
  #insert query
  insertResultQuery = "INSERT INTO test_result (testTimestamp, downloadSpeed, uploadSpeed) VALUES (%s, %s, %s)"
  tqParam =  (resultTuple[0].strftime("%Y-%m-%d %H:%M:%S"), resultTuple[1], resultTuple[2])  #MySQL requires datetime format as "YYYY-MM-DD HH:MM:SS"
  print(tqParam)

  getAverageQuery = "SELECT AVG(downloadSpeed) AS Avg_Download FROM test_result"
  dbCursor = mydb.cursor()

  dbCursor.execute(setDB) #use speedtestDB
  dbCursor.execute(insertResultQuery, tqParam) #run the test query
  dbCursor.execute(getAverageQuery) #get the average download speed
  
  average = dbCursor.fetchone()[0]
  print("Average speed across all tests ran: " + str(average))

  mydb.commit()  #commit changes and close
  mydb.close()


if __name__ == "__main__":
  main()
