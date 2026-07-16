class Solution:
    def countStudents(self, students, sandwiches):
        from collections import Counter
        c=Counter(students)
        for i,x in enumerate(sandwiches):
            if not c[x]:return len(students)-i
            c[x]-=1
        return 0
