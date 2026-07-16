class Solution:
    def destCity(self, paths):
        starts = {start for start, _ in paths}
        return next(end for _, end in paths if end not in starts)
