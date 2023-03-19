import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('sonarshubham101@gmail.com','Shubham@1001')
subject="testing mail python"

body='''
Hello ,my name is shubham more and i am automation tester with experience in ETL and SQL.
as and automation tester I am expert in designing and implementing automated tests to ensure the quality of software application.I have experience using variety of testing tools and frameworks including selenium,pytest,pandas,python ,beautifulsoup,openpyxl
I also know about ETL process.I am familiar with tools like tablue,power BI,informatica,visual studio
I also have experience working with database including oracle,SQL server.I can write complex query for data analysis using SQL
'''
massage="subject:{}\n\n{}".format(subject,body)
listadd=['priyankaec24@gmail.com','rautkshitija04@gmail.com','apekshakhbrgd@gmail.com','sohelnaikwade85@gmail.com']
ob.sendmail('priyankaec24@gmail.com',listadd,massage)
print("send mail ")
ob.quit()