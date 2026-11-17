# Problem: Simplify Path
# Platform: LeetCode
# Difficulty: Medium

class Solution:
    def simplifyPath(self, path):
        stack = []

        folders = path.split("/")

        for folder in folders:
            if folder == "" or folder == ".":
                continue

            elif folder == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(folder)

        return "/" + "/".join(stack)
