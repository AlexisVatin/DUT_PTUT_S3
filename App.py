import sys
import getopt
from gui.main_window import MainWindow

# def main(argv):
#     try:
#         opts, args = getopt.getopt(argv, "hf:", ["file="])
#     except getopt.GetoptError:
#         sys.exit(2)
#
#     for opt, arg in opts:
#         if opt == '-h':
#             print('test.py -f <file>')
#             sys.exit()
#         elif opt in ("-f", "--file"):
#             print(arg)
#
#
# if __name__ == "__main__":
#     main(sys.argv[1:])
#     listTempo = ["astronogeek"] # Liste dynamique a changer apres
#     bot = Bot(listTempo, "drivers\chromedriver.exe")
#     bot.execute()

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
