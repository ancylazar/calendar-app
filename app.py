from datetime import datetime


class Calendar:
    def __init__(self):
        self.events = []
        self.next_id = 1

    def add_event(self, title, date, time):
        event = {
            "id": self.next_id,
            "title": title,
            "date": date,
            "time": time
        }
        self.events.append(event)
        self.next_id += 1
        return event

    def edit_event(self, event_id, title, date, time):
        for event in self.events:
            if event["id"] == event_id:
                event["title"] = title
                event["date"] = date
                event["time"] = time
                return True
        return False

    def delete_event(self, event_id):
        for event in self.events:
            if event["id"] == event_id:
                self.events.remove(event)
                return True
        return False

    def view_events(self):
        return self.events


def main():
    calendar = Calendar()

    while True:
        print("\n===== CALENDAR APPLICATION =====")
        print("1. Add Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. View Events")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter event title: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")

            try:
                datetime.strptime(date, "%Y-%m-%d")
                datetime.strptime(time, "%H:%M")
            except ValueError:
                print("Invalid date or time format.")
                continue

            event = calendar.add_event(title, date, time)
            print(f"Event added successfully! ID: {event['id']}")

        elif choice == "2":
            try:
                event_id = int(input("Enter event ID to edit: "))
            except ValueError:
                print("Invalid event ID.")
                continue

            title = input("Enter new title: ")
            date = input("Enter new date (YYYY-MM-DD): ")
            time = input("Enter new time (HH:MM): ")

            try:
                datetime.strptime(date, "%Y-%m-%d")
                datetime.strptime(time, "%H:%M")
            except ValueError:
                print("Invalid date or time format.")
                continue

            if calendar.edit_event(event_id, title, date, time):
                print("Event updated successfully!")
            else:
                print("Event not found.")

        elif choice == "3":
            try:
                event_id = int(input("Enter event ID to delete: "))
            except ValueError:
                print("Invalid event ID.")
                continue

            if calendar.delete_event(event_id):
                print("Event deleted successfully!")
            else:
                print("Event not found.")

        elif choice == "4":
            events = calendar.view_events()

            if not events:
                print("No events available.")
            else:
                for event in events:
                    print(
                        f"ID: {event['id']} | "
                        f"Title: {event['title']} | "
                        f"Date: {event['date']} | "
                        f"Time: {event['time']}"
                    )

        elif choice == "5":
            print("Thank you for using Calendar Application!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
