# LeetCode 1622 - Fancy Sequence
# https://leetcode.com/problems/fancy-sequence/

class Fancy
  MOD = 1_000_000_007

  def initialize
    @n = 0
    @size = 1 << 17
    @tree = Array.new(2 * @size, 0)
    @mul = Array.new(2 * @size, 1)
    @add = Array.new(2 * @size, 0)
  end

  def append(val)
    _update(1, 0, @size - 1, @n, @n, 0, val % MOD)
    @n += 1
    nil
  end

  def add_all(inc)
    _update(1, 0, @size - 1, 0, @n - 1, 1, inc % MOD) if @n.positive?
    nil
  end

  def mult_all(m)
    _update(1, 0, @size - 1, 0, @n - 1, m % MOD, 0) if @n.positive?
    nil
  end

  def get_index(idx)
    idx < @n ? _get(1, 0, @size - 1, idx) : -1
  end

  private

  def _apply(p, m, a)
    @tree[p] = (@tree[p] * m + a) % MOD
    @mul[p] = @mul[p] * m % MOD
    @add[p] = (@add[p] * m + a) % MOD
  end

  def _push(p)
    return unless @mul[p] != 1 || @add[p] != 0

    _apply(2 * p, @mul[p], @add[p])
    _apply(2 * p + 1, @mul[p], @add[p])
    @mul[p] = 1
    @add[p] = 0
  end

  def _update(p, l, r, ql, qr, m, a)
    if ql <= l && r <= qr
      _apply(p, m, a)
      return
    end
    _push(p)
    mid = (l + r) / 2
    _update(2 * p, l, mid, ql, qr, m, a) if ql <= mid
    _update(2 * p + 1, mid + 1, r, ql, qr, m, a) if qr > mid
  end

  def _get(p, l, r, i)
    return @tree[p] if l == r

    _push(p)
    mid = (l + r) / 2
    i <= mid ? _get(2 * p, l, mid, i) : _get(2 * p + 1, mid + 1, r, i)
  end
end
