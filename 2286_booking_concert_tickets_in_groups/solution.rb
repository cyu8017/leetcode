# LeetCode 2286 - Booking Concert Tickets in Groups
# https://leetcode.com/problems/booking-concert-tickets-in-groups/

class BookMyShow
  def initialize(n, m)
    @n = n
    @m = m
    @sum = Array.new(4 * n, 0)
    @mx = Array.new(4 * n, 0)
    build(1, 0, n - 1)
  end

  def gather(k, max_row)
    row = find_first(1, 0, @n - 1, max_row, k)
    return [] if row == -1

    remain = query_sum(1, 0, @n - 1, row, row)
    seat = @m - remain
    update(1, 0, @n - 1, row, remain - k)
    [row, seat]
  end

  def scatter(k, max_row)
    return false if query_sum(1, 0, @n - 1, 0, max_row) < k

    need = k
    row = 0
    while row <= max_row && need > 0
      remain = query_sum(1, 0, @n - 1, row, row)
      if remain != 0
        take = [remain, need].min
        update(1, 0, @n - 1, row, remain - take)
        need -= take
      end
      row += 1
    end
    true
  end

  private

  def pull(idx)
    @sum[idx] = @sum[idx * 2] + @sum[idx * 2 + 1]
    @mx[idx] = [@mx[idx * 2], @mx[idx * 2 + 1]].max
  end

  def build(idx, l, r)
    if l == r
      @sum[idx] = @mx[idx] = @m
      return
    end
    mid = (l + r) >> 1
    build(idx * 2, l, mid)
    build(idx * 2 + 1, mid + 1, r)
    pull(idx)
  end

  def update(idx, l, r, pos, val)
    if l == r
      @sum[idx] = @mx[idx] = val
      return
    end
    mid = (l + r) >> 1
    if pos <= mid
      update(idx * 2, l, mid, pos, val)
    else
      update(idx * 2 + 1, mid + 1, r, pos, val)
    end
    pull(idx)
  end

  def query_sum(idx, l, r, ql, qr)
    return 0 if qr < l || r < ql
    return @sum[idx] if ql <= l && r <= qr

    mid = (l + r) >> 1
    query_sum(idx * 2, l, mid, ql, qr) + query_sum(idx * 2 + 1, mid + 1, r, ql, qr)
  end

  def find_first(idx, l, r, max_row, k)
    return -1 if l > max_row || @mx[idx] < k
    return l if l == r

    mid = (l + r) >> 1
    left = find_first(idx * 2, l, mid, max_row, k)
    return left unless left == -1

    find_first(idx * 2 + 1, mid + 1, r, max_row, k)
  end
end
