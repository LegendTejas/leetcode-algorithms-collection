# Boyer-Moore Majority Vote Algorithm

## 📌 Overview
The **Boyer-Moore Majority Vote Algorithm** is a linear-time, constant-space algorithm 
to find the majority element(s) in an array.

- **Majority Element**: An element that appears **more than ⌊n/2⌋ times**.
- **Generalization**: Can also be extended to find elements appearing **more than ⌊n/3⌋ times**.

### ✅ Advantages
- Time Complexity: **O(n)**
- Space Complexity: **O(1)**
- Elegant use of *counting votes*.

---

## 🔑 Key Intuition
- When elements cancel each other out (vote +1 and -1), only the **majority element** can remain in the end.
- Works in **two passes**:
  1. Find a candidate.
  2. Verify if it’s truly the majority.

---

## 📚 Problems Included
1. **LeetCode 169 - Majority Element**  
2. **LeetCode 229 - Majority Element II**  
3. **Extended Notes** (edge cases, multiple majority thresholds)
