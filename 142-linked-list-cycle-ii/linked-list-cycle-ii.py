class Solution(object):
    def detectCycle(self, head):

        slow = head
        fast = head

        # Find whether a cycle exists
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        # No cycle
        if not fast or not fast.next:
            return None

        # Find the starting node of cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
        