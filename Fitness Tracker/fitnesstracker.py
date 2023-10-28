class FitnessTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, duration):
        self.activities.append({"activity": activity, "duration": duration})

    def view_activities(self):
        for index, entry in enumerate(self.activities, start=1):
            print(f"{index}. Activity: {entry['activity']}, Duration: {entry['duration']} minutes")

    def total_duration(self):
        total = sum(entry["duration"] for entry in self.activities)
        print(f"Total Duration: {total} minutes")

def main():
    tracker = FitnessTracker()
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. View Total Duration")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            activity = input("Enter the activity: ")
            duration = int(input("Enter the duration in minutes: "))
            tracker.add_activity(activity, duration)
        elif choice == '2':
            print("\nList of Activities:")
            tracker.view_activities()
        elif choice == '3':
            tracker.total_duration()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
