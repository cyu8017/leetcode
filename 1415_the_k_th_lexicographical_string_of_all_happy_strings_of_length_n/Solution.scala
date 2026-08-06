object Solution {
  def getHappyString(n: Int, k: Int): String = { val out=scala.collection.mutable.ArrayBuffer[String](); def dfs(s:String):Unit = if(s.length==n)out+=s else "abc".filter(c=>s.isEmpty||s.last!=c).foreach(c=>dfs(s+c)); dfs(""); if(k<=out.length)out(k-1) else "" }
}
