
# Press the green button in the gutter to run the script.
from systems.Visual.GUI import GUI
from systems.Searcher import Searcher

if __name__ == '__main__':
    test = Searcher()
    gui = GUI()

    testcase2 = test.rank_words(["I","I","U","O","E","O","R"])
    print(testcase2)
    print(test.must_include_dict(testcase2,"R"))

    while gui.running:
        gui.update()
    gui.killApp()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
