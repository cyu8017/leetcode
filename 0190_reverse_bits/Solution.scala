object Solution { def reverseBits(n: Int): Int = { var x = n; var ans = 0; for (_ <- 0 until 32) { ans = (ans << 1) | (x & 1); x = x >>> 1 }; ans } }
