# LeetCode 1912 - Design Movie Rental System
# https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem
  # @param {Integer} n
  # @param {Integer[][]} entries
  def initialize(n, entries)
    @price = {}
    @available = Hash.new { |h, k| h[k] = [] }
    @rented = []
    entries.each do |shop, movie, price|
      @price[[shop, movie]] = price
      insort(@available[movie], [price, shop])
    end
  end

  # @param {Integer} movie
  # @return {Integer[]}
  def search(movie)
    @available[movie].first(5).map { |_, shop| shop }
  end

  # @param {Integer} shop
  # @param {Integer} movie
  # @return {Void}
  def rent(shop, movie)
    price = @price[[shop, movie]]
    @available[movie].delete([price, shop])
    insort(@rented, [price, shop, movie])
    nil
  end

  # @param {Integer} shop
  # @param {Integer} movie
  # @return {Void}
  def drop(shop, movie)
    price = @price[[shop, movie]]
    @rented.delete([price, shop, movie])
    insort(@available[movie], [price, shop])
    nil
  end

  # @return {Integer[][]}
  def report
    @rented.first(5).map { |_, shop, movie| [shop, movie] }
  end

  private

  def insort(arr, item)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] < item
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.insert(lo, item)
  end
end
