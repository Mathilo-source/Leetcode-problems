
package circle;
import java.util.Scanner;

// Circular Queue Implementation
class MyCircularQueue {
    private int[] queue;
    private int front;
    private int rear;
    private int size;
    private int capacity;

    // Constructor
    public MyCircularQueue(int k) {
        queue = new int[k];
        capacity = k;
        front = 0;
        rear = -1;
        size = 0;
    }

    // Insert element into the circular queue
    public boolean enQueue(int value) {
        if (isFull()) {
            return false;
        }
        rear = (rear + 1) % capacity;
        queue[rear] = value;
        size++;
        return true;
    }

    // Delete element from the circular queue
    public boolean deQueue() {
        if (isEmpty()) {
            return false;
        }
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    // Get the front item
    public int Front() {
        if (isEmpty()) return -1;
        return queue[front];
    }

    // Get the last item
    public int Rear() {
        if (isEmpty()) return -1;
        return queue[rear];
    }

    // Check if queue is empty
    public boolean isEmpty() {
        return size == 0;
    }

    // Check if queue is full
    public boolean isFull() {
        return size == capacity;
    }
}

// Main class for user interaction
public class Circle 
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of Circular Queue: ");
        int k = sc.nextInt();

        MyCircularQueue myQueue = new MyCircularQueue(k);

        while (true) {
            System.out.println("\n--- Circular Queue Menu ---");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Front");
            System.out.println("4. Rear");
            System.out.println("5. Check if Empty");
            System.out.println("6. Check if Full");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");

            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value to enqueue: ");
                    int value = sc.nextInt();
                    if (myQueue.enQueue(value))
                        System.out.println(value + " enqueued successfully.");
                    else
                        System.out.println("Queue is FULL! Cannot enqueue.");
                    break;

                case 2:
                    if (myQueue.deQueue())
                        System.out.println("Dequeued successfully.");
                    else
                        System.out.println("Queue is EMPTY! Cannot dequeue.");
                    break;

                case 3:
                    System.out.println("Front element: " + myQueue.Front());
                    break;

                case 4:
                    System.out.println("Rear element: " + myQueue.Rear());
                    break;

                case 5:
                    System.out.println("Is Empty? " + myQueue.isEmpty());
                    break;

                case 6:
                    System.out.println("Is Full? " + myQueue.isFull());
                    break;

                case 7:
                    System.out.println("Exiting program...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}

