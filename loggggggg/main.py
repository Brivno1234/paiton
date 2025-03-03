#fail.read()
#fail.close()
#fail.write()
import log_panser as logs
import report_generator as generateReport

log_file = "logs.txt"

result = logs.analyse_log(log_file)
generateReport.generate_report(result)

#generate_report()

#with open("file.txt","r",encoding="utf-8") as file:
