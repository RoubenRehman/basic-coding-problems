from pyclbr import Function
from merge_sorted_lists import merge_sorted_lists
from reverse_list import reverse_list
from ListHelpers.ListHelpers import ListNode, print_list, builtin_to_list

class SolutionChecker:
    def __init__(self) -> None:
        self.impls = []
        self.tests = []
        self.fails = []

    def register_solution(self, impl: Function, test: list) -> bool:
        if not impl or not test:
            return False
        
        self.impls.append(impl)
        self.tests.append(test)

        return True

    def run(self) -> None:
        for idx, test in enumerate(self.tests):
            print("++++++ Testing " + self.impls[idx].__name__ + " ++++++")
            for idy, case in enumerate(test[0]):
                print("Test case " + str(idy))
                res = self.impls[idx](*case)
                if res == test[1][idy]:
                    print("Test successfull")
                else:
                    print("Test unsuccessfull")
                    self.fails.append([self.impls[idx].__name__, idy])

        print("")
        while self.fails:
            fail = self.fails.pop()
            print("Failed test for function: " + fail[0], " Case: " + str(fail[1] + 1))
            
test1 = [
    [[builtin_to_list([1, 2, 3])], [builtin_to_list([4, 7, 9, 12])]],
    [builtin_to_list([3, 2, 1]), builtin_to_list([12, 9, 7, 4])]
]
print(test1[0])
checker = SolutionChecker()
checker.register_solution(reverse_list, test1)
checker.run()



    