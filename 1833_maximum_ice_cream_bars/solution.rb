
# @param {Integer[]} costs
# @param {Integer} coins
# @return {Integer}
def max_ice_cream(costs, coins)
  costs = costs.sort
  count = 0
  costs.each do |cost|
    break if coins < cost
    coins -= cost
    count += 1
  end
  count
end
