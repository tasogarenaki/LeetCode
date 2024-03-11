import java.util.HashMap;

class twoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int targNum = target - num;
            if (map.containsKey(targNum)) {
                return new int[]{map.get(targNum), i};
            }
            map.put(num, i);
        }

        return new int[]{-1, -1};   //If no solution is found
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        twoSum solution = new twoSum();
        int[] result = solution.twoSum(nums, target);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }
}
