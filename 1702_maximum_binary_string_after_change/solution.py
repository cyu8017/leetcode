class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        zeros = binary.count("0")
        if zeros <= 1:
            return binary
        first = binary.find("0")
        return "1" * (first + zeros - 1) + "0" + "1" * (len(binary) - first - zeros)
