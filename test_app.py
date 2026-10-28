import unittest
from app import Calendar
class TestCalendar(unittest.TestCase):

    def setUp(self):
        self.calendar = Calendar()

    def test_add_event(self):
        event = self.calendar.add_event(
            "Project Review", "2026-11-05", "10:00"
        )
        self.assertEqual(event["title"], "Project Review")
        self.assertEqual(len(self.calendar.view_events()), 1)

    def test_edit_event(self):
        event = self.calendar.add_event(
            "Meeting", "2026-11-05", "10:00"
        )
        result = self.calendar.edit_event(
            event["id"], "Team Meeting", "2026-11-06", "11:00"
        )
        self.assertTrue(result)
        self.assertEqual(
            self.calendar.view_events()[0]["title"], "Team Meeting"
        )

    def test_delete_event(self):
        event = self.calendar.add_event(
            "Appointment", "2026-11-05", "14:00"
        )
        result = self.calendar.delete_event(event["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.calendar.view_events()), 0)


if __name__ == "__main__":
    unittest.main()