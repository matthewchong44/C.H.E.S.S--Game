from  selenium import webdriver
import Convertor
import sys
# sys.path.append(r"C:\Users\Owner\Documents\GitHub\C.H.E.S.S--Game\js")
# print("\nPaths\n")
# print(sys.path)
# print("\n"):
# import Bishop.js as Bishop
# #Board,King,Knight,main,Pawn,Piece,Queen,Rook

driver = webdriver.Chrome(executable_path=r'C:\Users\Owner\Documents\GitHub\C.H.E.S.S--Game\Selenium\drivers\chromedriver.exe')
driver.set_page_load_timeout(10)

driver.get("http://127.0.0.1:5000/")


def pawnMovement():
    driver.find_element_by_class_name("btn").click()
    driver.find_element_by_id("21").click()
    #driver.find_element_by_id("31").click()
    return

pawnMovement()
