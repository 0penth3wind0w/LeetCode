class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # directedAdjMatrix[course_i][course_j] == True when course_j is a prerequisite of course_i
        directedAdjMatrix = [[None for _ in range(numCourses)] for _ in range(numCourses)]
        # update prerequisites
        for prereq in prerequisites:
            directedAdjMatrix[prereq[1]][prereq[0]] = True

        # check if qCourse is a prerequisite of course
        def isPrereq(qCourse, course):
            # print(f"{qCourse=}, {course=}")
            if directedAdjMatrix[course][qCourse] is None:
                for pCourse, result in enumerate(directedAdjMatrix[course]):
                    if result and isPrereq(qCourse, pCourse):
                        directedAdjMatrix[course][qCourse] = True
                        break
                else:
                    directedAdjMatrix[course][qCourse] = False
            return directedAdjMatrix[course][qCourse]

        return [isPrereq(q[0], q[1]) for q in queries]
