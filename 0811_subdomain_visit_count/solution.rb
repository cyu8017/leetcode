# LeetCode 0811 - Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/

# @param {String[]} cpdomains
# @return {String[]}
def subdomain_visits(cpdomains)
  counts = Hash.new(0)
  cpdomains.each do |item|
    count_str, domain = item.split
    count = count_str.to_i
    parts = domain.split(".")
    parts.length.times { |i| counts[parts[i..].join(".")] += count }
  end
  counts.map { |domain, count| "#{count} #{domain}" }
end
