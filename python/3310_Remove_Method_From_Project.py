# Leetcode 3310: Remove Method From Project
# Difficulty : Medium
# Language : Python

from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v) 
            reverse[v].append(u)
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)
        for i in range(n):
            if suspicious[i]:
                for p in reverse[i]:
                    if not suspicious[p]:
                        return list(range(n))
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)
        return ans
