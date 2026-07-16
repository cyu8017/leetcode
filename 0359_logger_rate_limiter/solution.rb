# LeetCode 0359 - Logger Rate Limiter
# https://leetcode.com/problems/logger-rate-limiter/

class Logger
  def initialize
    @last_printed = {}
  end

  def should_print_message(timestamp, message)
    if !@last_printed.key?(message) || timestamp - @last_printed[message] >= 10
      @last_printed[message] = timestamp
      return true
    end

    false
  end

  alias_method :shouldPrintMessage, :should_print_message
end
