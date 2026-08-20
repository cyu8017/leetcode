// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

type SQL struct {
	tables map[string][][]string
	nextID map[string]int
}

func Constructor(names []string, columns []int) SQL {
	s := SQL{tables: map[string][][]string{}, nextID: map[string]int{}}
	for _, name := range names {
		s.tables[name] = [][]string{}
		s.nextID[name] = 1
	}
	return s
}

func (this *SQL) Ins(name string, row []string) bool {
	if _, ok := this.tables[name]; !ok {
		return false
	}
	id := this.nextID[name]
	this.nextID[name]++
	full := append([]string{itoa(id)}, row...)
	this.tables[name] = append(this.tables[name], full)
	return true
}

func (this *SQL) Rmv(name string, rowId int) {
	rows := this.tables[name]
	for i, r := range rows {
		if atoi(r[0]) == rowId {
			this.tables[name] = append(rows[:i], rows[i+1:]...)
			return
		}
	}
}

func (this *SQL) Sel(name string, rowId int, columnId int) string {
	for _, r := range this.tables[name] {
		if atoi(r[0]) == rowId {
			if columnId < 1 || columnId >= len(r) {
				return "<null>"
			}
			return r[columnId]
		}
	}
	return "<null>"
}

func (this *SQL) Exp(name string) []string {
	rows := this.tables[name]
	ans := make([]string, len(rows))
	for i, r := range rows {
		s := r[0]
		for j := 1; j < len(r); j++ {
			s += "," + r[j]
		}
		ans[i] = s
	}
	return ans
}

func itoa(x int) string {
	if x == 0 {
		return "0"
	}
	b := []byte{}
	for x > 0 {
		b = append([]byte{byte('0' + x%10)}, b...)
		x /= 10
	}
	return string(b)
}

func atoi(s string) int {
	x := 0
	for i := 0; i < len(s); i++ {
		x = x*10 + int(s[i]-'0')
	}
	return x
}
