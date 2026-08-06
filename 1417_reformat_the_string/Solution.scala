object Solution {
  def reformat(s: String): String = { var a=s.filter(_.isLetter); var b=s.filter(_.isDigit); if(math.abs(a.length-b.length)>1)"" else { if(b.length>a.length){val t=a;a=b;b=t}; a.indices.map(i=>a(i).toString+(if(i<b.length)b(i).toString else "")).mkString } }
}
