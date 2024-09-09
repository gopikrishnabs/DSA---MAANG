class Solution:
    def canVisitAllRoomsDFS(self, rooms: list[list[int]]) -> bool:
        
        N = len(rooms)
        roomUnlocked = [False]*N

        def dfs(room):
            if roomUnlocked[room]:
                return 
            
            if not roomUnlocked[room]:
                roomUnlocked[room] = True

            for adjacent in rooms[room]:
                dfs(adjacent)
        
        dfs(0)

        return all(unLockedStatus for unLockedStatus in roomUnlocked)

    def canVisitAllRoomsBFS(self, rooms: list[list[int]]) -> bool:
        
        N = len(rooms)
        roomUnlocked = [False]*N

        queue = deque([0])

        while queue:
            room = queue.popleft()
            if roomUnlocked[room]:
                continue
            
            if not roomUnlocked[room]:
                roomUnlocked[room] = True
            

            for adjacent in rooms[room]:
                queue.append(adjacent)

        return all(unLockedStatus for unLockedStatus in roomUnlocked)


if __name__ == "__main__":
    solutionObject = Solution()
    print(solutionObject.canVisitAllRoomsDFS([[1],[2],[3],[]]), solutionObject.canVisitAllRoomsBFS([[1],[2],[3],[]]))
