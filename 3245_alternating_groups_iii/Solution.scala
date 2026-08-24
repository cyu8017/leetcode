// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

object Solution {
  class SegTree(n_ : Int) {
    val n = n_
    val treeIntervalCounts = new Array[Int](4 * n_)
    val treeIntervalLengths = new Array[Int](4 * n_)
    def add(i: Int, v: Int): Unit = addRec(0, 0, n - 1, i, v)
    def addRec(treeIndex: Int, lo: Int, hi: Int, i: Int, v: Int): Unit = {
      if (lo == hi) {
        treeIntervalCounts(treeIndex) += v
        treeIntervalLengths(treeIndex) = treeIntervalCounts(treeIndex) * i
        return
      }
      val mid = (lo + hi) / 2
      if (i <= mid) addRec(2 * treeIndex + 1, lo, mid, i, v)
      else addRec(2 * treeIndex + 2, mid + 1, hi, i, v)
      treeIntervalCounts(treeIndex) = treeIntervalCounts(2 * treeIndex + 1) + treeIntervalCounts(2 * treeIndex + 2)
      treeIntervalLengths(treeIndex) = treeIntervalLengths(2 * treeIndex + 1) + treeIntervalLengths(2 * treeIndex + 2)
    }
    def queryIntervalCounts(i: Int): Int = query(treeIntervalCounts, 0, 0, n - 1, i, n - 1)
    def queryIntervalLengths(i: Int): Int = query(treeIntervalLengths, 0, 0, n - 1, i, n - 1)
    def query(tree: Array[Int], treeIndex: Int, lo: Int, hi: Int, i: Int, j: Int): Int = {
      if (i <= lo && hi <= j) return tree(treeIndex)
      if (j < lo || hi < i) return 0
      val mid = (lo + hi) / 2
      query(tree, treeIndex * 2 + 1, lo, mid, i, j) + query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j)
    }
  }

  def pack(l: Int, r: Int): Long = (l.toLong << 32) | (r & 0xffffffffL)
  def unpackL(v: Long): Int = (v >> 32).toInt
  def unpackR(v: Long): Int = v.toInt

  def numberOfAlternatingGroups(colors: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val n = colors.length
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    val arr = new Array[Int](2 * n - 1)
    var i = 0
    while (i < n) { arr(i) = colors(i); i += 1 }
    i = 0
    while (i < n - 1) { arr(n + i) = colors(i); i += 1 }
    val tree = new SegTree(2 * n - 1)
    val intervals = scala.collection.mutable.TreeSet.empty[Long]

    def insert(l: Int, r: Int): Unit = {
      intervals += pack(l, r)
      if (l < n) tree.add(r - l + 1, 1)
    }
    def remove(l: Int, r: Int): Unit = {
      intervals -= pack(l, r)
      if (l < n) tree.add(r - l + 1, -1)
    }
    def findInterval(target: Int): Array[Int] = {
      var bestL = -1
      var bestR = -1
      for (k <- intervals) {
        val kl = unpackL(k)
        val kr = unpackR(k)
        if (kl <= target && target <= kr && kl > bestL) {
          bestL = kl
          bestR = kr
        }
      }
      Array(bestL, bestR)
    }
    def getNum(sz: Int): Int = {
      val numIntervals = tree.queryIntervalCounts(sz)
      val sumIntervals = tree.queryIntervalLengths(sz)
      var numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals
      val lr = findInterval(n)
      val l = lr(0)
      val r = lr(1)
      if (l < 0 || l >= n || r - l + 1 < sz) return numAlternatingGroups
      if (r >= n) {
        val nonDuplicateGroups = n - l
        val numGroups = (r - l + 1) - sz + 1
        val extra = numGroups - nonDuplicateGroups
        if (extra > 0) numAlternatingGroups -= extra
      }
      numAlternatingGroups
    }
    def update(index: Int, color: Int): Unit = {
      if (arr(index) == color) return
      arr(index) = color
      val se = findInterval(index)
      val start = se(0)
      val end = se(1)
      remove(start, end)
      if (start < index && index < end) {
        insert(start, index - 1)
        insert(index, index)
        insert(index + 1, end)
        return
      }
      if (start == index && index < end) insert(start + 1, end)
      if (start < index && index == end) insert(start, end - 1)
      var ns = index
      var ne = index
      var merged = true
      while (merged) {
        merged = false
        val snap = intervals.toArray
        var si = 0
        while (si < snap.length && !merged) {
          val kl = unpackL(snap(si))
          val kr = unpackR(snap(si))
          if (kr + 1 == ns && arr(kr) != arr(ns)) {
            remove(kl, kr)
            ns = kl
            merged = true
          }
          si += 1
        }
      }
      merged = true
      while (merged) {
        merged = false
        val snap = intervals.toArray
        var si = 0
        while (si < snap.length && !merged) {
          val kl = unpackL(snap(si))
          val kr = unpackR(snap(si))
          if (kl == ne + 1 && arr(kl) != arr(ne)) {
            remove(kl, kr)
            ne = kr
            merged = true
          }
          si += 1
        }
      }
      insert(ns, ne)
    }

    var st = 0
    i = 1
    while (i < 2 * n - 1) {
      if (arr(i) == arr(i - 1)) {
        insert(st, i - 1)
        st = i
      }
      i += 1
    }
    insert(st, 2 * n - 2)
    for (query <- queries) {
      if (query(0) == 1) ans += getNum(query(1))
      else {
        val index = query(1)
        val color = query(2)
        if (arr(index) != color) {
          update(index, color)
          if (index < n - 1) update(index + n, color)
        }
      }
    }
    ans.toArray
  }
}
