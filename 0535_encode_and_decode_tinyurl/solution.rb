# LeetCode 0535 - Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec
  def initialize
    @url_to_code = {}
    @code_to_url = {}
    @counter = 0
    @base = "http://tinyurl.com/"
  end

  def encode(long_url)
    return @url_to_code[long_url] if @url_to_code.key?(long_url)

    code = @counter.to_s
    @counter += 1
    short_url = @base + code
    @url_to_code[long_url] = short_url
    @code_to_url[short_url] = long_url
    short_url
  end

  def decode(short_url)
    @code_to_url[short_url]
  end
end
