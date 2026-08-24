# LeetCode 2979 - Most Expensive Item That Can Not Be Bought
# https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/

# @param {Integer} prime_one
# @param {Integer} prime_two
# @return {Integer}
def most_expensive_item(prime_one, prime_two)
  prime_one * prime_two - prime_one - prime_two
end

def solve(*args)
  most_expensive_item(*args)
end
