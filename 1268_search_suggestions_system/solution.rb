# LeetCode 1268 - Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/

# @param {String[]} products
# @param {String} search_word
# @return {String[][]}
def suggested_products(products, search_word)
  products = products.sort
  answer = []
  prefix = ""
  search_word.each_char do |ch|
    prefix += ch
    i = products.bsearch_index { |p| p >= prefix } || products.length
    answer << products[i, 3].select { |p| p.start_with?(prefix) }
  end
  answer
end
