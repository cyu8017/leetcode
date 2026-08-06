object Solution {
  def minNumberOfFrogs(croakOfFrogs: String): Int = { val ix=Map('c'->0,'r'->1,'o'->2,'a'->3,'k'->4); val c=Array.fill(5)(0); var active=0; var ans=0; for(ch <- croakOfFrogs) { if(!ix.contains(ch))return -1; val i=ix(ch); if(i>0 && c(i-1)==0)return -1; if(i>0)c(i-1)-=1; c(i)+=1; if(i==0){active+=1;ans=math.max(ans,active)} else if(i==4){c(4)-=1;active-=1} }; if(active==0)ans else -1 }
}
