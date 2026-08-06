# LeetCode 1236 - Web Crawler
# https://leetcode.com/problems/web-crawler/

require "uri"
require "set"

# @param {String} start_url
# @param {HtmlParser} html_parser
# @return {String[]}
def crawl(start_url, html_parser)
  host = URI.parse(start_url).host
  seen = Set[start_url]
  stack = [start_url]
  until stack.empty?
    html_parser.getUrls(stack.pop).each do |url|
      if URI.parse(url).host == host && !seen.include?(url)
        seen.add(url)
        stack << url
      end
    end
  end
  seen.to_a.sort
end
