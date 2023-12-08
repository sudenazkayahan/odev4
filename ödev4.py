cevap 1:
class Solution:
    def twoSum(self, nums, target):
        # Boş bir sözlük oluşturulur
        num_dict = {}

        # Tamsayı dizisi üzerinde dönülür
        for i, num in enumerate(nums):
            # Hedeften mevcut sayıyı çıkartarak eşleşen sayıyı bulmaya çalışırız
            complement = target - num
            
            # Eşleşen sayı sözlükte varsa, çözümü döndürürüz
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Eşleşen sayı yoksa, mevcut sayıyı sözlüğe ekleriz
            num_dict[num] = i

cevap 2:
class Solution:
    def threeSum(self, nums):
        nums.sort()  # Dizi sıralanır
        result = []  # Sonuç listesi

        for i in range(len(nums) - 2):
            # Aynı sayıdan kaçınılır
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])

                    # Aynı sayıdan kaçınılır
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return result

cevap 3:
class PhoneKeypad:
    def __init__(self):
        self.keypad = {
            'a': 2, 'b': 2, 'c': 2,
            'd': 3, 'e': 3, 'f': 3,
            'g': 4, 'h': 4, 'i': 4,
            'j': 5, 'k': 5, 'l': 5,
            'm': 6, 'n': 6, 'o': 6,
            'p': 7, 'q': 7, 'r': 7, 's': 7,
            't': 8, 'u': 8, 'v': 8,
            'w': 9, 'x': 9, 'y': 9, 'z': 9
        }

    def textToKeypad(self, text):
        result = []

        for char in text:
            if char == ' ':
                result.append(0)
            elif char.isdigit():
                result[-1].append(int(char))
            else:
                result.append(self.keypad[char])

        return result

cevap 4:
class WordSearch:
    def findWords(self, board, words):
        def dfs(board, word, i, j, k):
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], "/"
            found = dfs(board, word, i + 1, j, k + 1) or \
                    dfs(board, word, i - 1, j, k + 1) or \
                    dfs(board, word, i, j + 1, k + 1) or \
                    dfs(board, word, i, j - 1, k + 1)

            board[i][j] = tmp
            return found

        result = []
        for word in words:
            found = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if dfs(board, word, i, j, 0):
                        found = True
                        break
                if found:
                    break
            if found:
                result.append(word)

        return result