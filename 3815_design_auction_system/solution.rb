# LeetCode 3815 - Design Auction System
# https://leetcode.com/problems/design-auction-system/

class AuctionSystem
  def initialize
    @items = Hash.new { |h, k| h[k] = [] }
    @users = {}
  end

  def add_bid(user_id, item_id, bid_amount)
    @users[user_id] ||= {}
    remove_bid(user_id, item_id) if @users[user_id].key?(item_id)
    @users[user_id][item_id] = bid_amount
    insert_sorted(@items[item_id], [bid_amount, user_id])
    nil
  end

  def update_bid(user_id, item_id, new_amount)
    old_amount = @users[user_id][item_id]
    remove_sorted(@items[item_id], [old_amount, user_id])
    insert_sorted(@items[item_id], [new_amount, user_id])
    @users[user_id][item_id] = new_amount
    nil
  end

  def remove_bid(user_id, item_id)
    old_amount = @users[user_id][item_id]
    remove_sorted(@items[item_id], [old_amount, user_id])
    @users[user_id].delete(item_id)
    nil
  end

  def get_highest_bidder(item_id)
    ls = @items[item_id]
    ls.empty? ? -1 : ls[-1][1]
  end

  private

  def insert_sorted(arr, pair)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < pair
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.insert(lo, pair)
  end

  def remove_sorted(arr, pair)
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < pair
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.delete_at(lo) if lo < arr.length && arr[lo] == pair
  end
end
