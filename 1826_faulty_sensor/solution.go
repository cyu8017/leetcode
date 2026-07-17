// LeetCode 1826 - Faulty Sensor
// https://leetcode.com/problems/faulty-sensor/

func badSensor(sensor1 []int, sensor2 []int) int {
	if slicesEqual(sensor1, sensor2) {
		return -1
	}

	isDefective := func(correct, faulty []int) bool {
		n := len(correct)
		i := 0
		for i < n && correct[i] == faulty[i] {
			i++
		}
		if i == n {
			return false
		}

		j := i
		for j < n-1 && correct[j+1] == faulty[j] {
			j++
		}
		return j == n-1
	}

	sensor1Bad := isDefective(sensor2, sensor1)
	sensor2Bad := isDefective(sensor1, sensor2)

	if sensor1Bad && sensor2Bad {
		return -1
	}
	if sensor1Bad {
		return 1
	}
	if sensor2Bad {
		return 2
	}
	return -1
}

func slicesEqual(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
