class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda t:t[1]-t[0],reverse=True)
        energy=spent=0
        for cost,minimum in tasks:
            energy=max(energy,spent+minimum);spent+=cost
        return energy
