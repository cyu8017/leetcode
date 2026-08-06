# LeetCode 1242 - Web Crawler Multithreaded
# https://leetcode.com/problems/web-crawler-multithreaded/

require "uri"
require "set"

# @param {String} start_url
# @param {HtmlParser} html_parser
# @return {String[]}
def crawl(start_url, html_parser)
  host = URI.parse(start_url).host
  seen = Set[start_url]
  frontier = [start_url]
  until frontier.empty?
    next_frontier = []
    frontier.each do |page|
      html_parser.getUrls(page).each do |url|
        if URI.parse(url).host == host && !seen.include?(url)
          seen.add(url)
          next_frontier << url
        end
      end
    end
    frontier = next_frontier
  end
  seen.to_a.sort
end
