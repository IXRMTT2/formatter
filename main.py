from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QSpinBox, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QMessageBox, QGridLayout, QGroupBox
)
from PyQt6.QtCore import Qt
import sys
from datetime import datetime


class DiscordMessageFormatter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Discord Message & Phase Log Formatter")

        main_layout = QVBoxLayout()

        discord_group = QGroupBox("Discord Message Format")
        discord_layout = QVBoxLayout()
        discord_grid = QGridLayout()
        row = 0

        discord_grid.addWidget(QLabel("HOST (@ tag):"), row, 0)
        self.host_input = QLineEdit()
        discord_grid.addWidget(self.host_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("TIMEZONE:"), row, 0)
        self.timezone_input = QLineEdit()
        self.timezone_input.setPlaceholderText("e.g. GMT")
        discord_grid.addWidget(self.timezone_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("START TIME (HH:MM am/pm):"), row, 0)
        self.start_time_input = QLineEdit()
        self.start_time_input.setPlaceholderText("e.g. 14:50 pm")
        discord_grid.addWidget(self.start_time_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("END TIME (HH:MM am/pm):"), row, 0)
        self.end_time_input = QLineEdit()
        self.end_time_input.setPlaceholderText("e.g. 15:15 pm")
        discord_grid.addWidget(self.end_time_input, row, 1)
        row += 1


        discord_grid.addWidget(QLabel("DURATION (mins):"), row, 0)
        self.duration_display = QLabel("0 mins")
        discord_grid.addWidget(self.duration_display, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("ATTENDEES:"), row, 0)
        self.attendees_input = QSpinBox()
        self.attendees_input.setRange(0, 1000)
        discord_grid.addWidget(self.attendees_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("PASSED:"), row, 0)
        self.passed_input = QSpinBox()
        self.passed_input.setRange(0, 1000)
        discord_grid.addWidget(self.passed_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("FAILED:"), row, 0)
        self.failed_input = QSpinBox()
        self.failed_input.setRange(0, 1000)
        discord_grid.addWidget(self.failed_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("Attendees List (one per line):"), row, 0, Qt.AlignmentFlag.AlignTop)
        self.attendees_list_input = QTextEdit()
        self.attendees_list_input.setPlaceholderText(
            "Format: username timezone, OR-#\nExample:\nFarhan_Unbeatable2 GMT, OR-6\nuwufurry_68, GMT, OR-2"
        )
        discord_grid.addWidget(self.attendees_list_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("SCHEDULED:"), row, 0)
        self.scheduled_input = QComboBox()
        self.scheduled_input.addItems(["No", "Yes"])
        discord_grid.addWidget(self.scheduled_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("NOTES:"), row, 0, Qt.AlignmentFlag.AlignTop)
        self.notes_input = QTextEdit()
        self.notes_input.setPlaceholderText("Any notes here...")
        discord_grid.addWidget(self.notes_input, row, 1)
        row += 1

        discord_grid.addWidget(QLabel("PROOF (user tags):"), row, 0, Qt.AlignmentFlag.AlignTop)
        self.proof_input = QTextEdit()
        self.proof_input.setPlaceholderText("e.g. @[RSM] DubyaYT @[RSM] MeerkatTDW @[RSM] ScriptHazed")
        discord_grid.addWidget(self.proof_input, row, 1)
        row += 1

        discord_layout.addLayout(discord_grid)

        self.generate_button = QPushButton("Generate Discord Message")
        discord_layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.generate_message)

        discord_layout.addWidget(QLabel("Generated Message:"))
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        discord_layout.addWidget(self.output_box)

        discord_group.setLayout(discord_layout)
        main_layout.addWidget(discord_group)

        phase_group = QGroupBox("Phase Log Format")
        phase_layout = QVBoxLayout()
        phase_grid = QGridLayout()
        prow = 0

        phase_grid.addWidget(QLabel("HOST (@ tag):"), prow, 0)
        self.phase_host_input = QLineEdit()
        phase_grid.addWidget(self.phase_host_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("TRAINING:"), prow, 0)
        self.training_input = QLineEdit()
        self.training_input.setPlaceholderText("e.g. Phase 1")
        phase_grid.addWidget(self.training_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("ATTENDEES:"), prow, 0)
        self.phase_attendees_input = QSpinBox()
        self.phase_attendees_input.setRange(0, 1000)
        phase_grid.addWidget(self.phase_attendees_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("PASSED:"), prow, 0)
        self.phase_passed_input = QSpinBox()
        self.phase_passed_input.setRange(0, 1000)
        phase_grid.addWidget(self.phase_passed_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("Attendees List (one per line):"), prow, 0, Qt.AlignmentFlag.AlignTop)
        self.phase_attendees_list_input = QTextEdit()
        self.phase_attendees_list_input.setPlaceholderText(
            "Format: username | TIMEZONE\nExample:\nIcetradez | EST"
        )
        phase_grid.addWidget(self.phase_attendees_list_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("FAILED:"), prow, 0)
        self.phase_failed_input = QSpinBox()
        self.phase_failed_input.setRange(0, 1000)
        phase_grid.addWidget(self.phase_failed_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("EVENT START TIME (HH:MM am/pm):"), prow, 0)
        self.event_start_input = QLineEdit()
        self.event_start_input.setPlaceholderText("e.g. 9:56 AM")
        phase_grid.addWidget(self.event_start_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("EVENT END TIME (HH:MM am/pm):"), prow, 0)
        self.event_end_input = QLineEdit()
        self.event_end_input.setPlaceholderText("e.g. 10:11 AM")
        phase_grid.addWidget(self.event_end_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("EVENT DURATION:"), prow, 0)
        self.event_duration_display = QLabel("0 minutes")
        phase_grid.addWidget(self.event_duration_display, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("NOTES:"), prow, 0, Qt.AlignmentFlag.AlignTop)
        self.phase_notes_input = QTextEdit()
        self.phase_notes_input.setPlaceholderText("Any notes here...")
        phase_grid.addWidget(self.phase_notes_input, prow, 1)
        prow += 1

        phase_grid.addWidget(QLabel("PING (user tags):"), prow, 0, Qt.AlignmentFlag.AlignTop)
        self.ping_input = QTextEdit()
        self.ping_input.setPlaceholderText("e.g. @[RSM] DubyaYT @[RSM] ScriptHazed @[RSM] MeerkatTDW")
        phase_grid.addWidget(self.ping_input, prow, 1)
        prow += 1

        phase_layout.addLayout(phase_grid)

        self.phase_generate_button = QPushButton("Generate Phase Log")
        phase_layout.addWidget(self.phase_generate_button)
        self.phase_generate_button.clicked.connect(self.generate_phase_log)

        phase_layout.addWidget(QLabel("Generated Phase Log Message:"))
        self.phase_output_box = QTextEdit()
        self.phase_output_box.setReadOnly(True)
        phase_layout.addWidget(self.phase_output_box)

        phase_group.setLayout(phase_layout)
        main_layout.addWidget(phase_group)

        self.setLayout(main_layout)
        self.resize(650, 900)

        self.start_time_input.editingFinished.connect(self.update_duration)
        self.end_time_input.editingFinished.connect(self.update_duration)
        self.event_start_input.editingFinished.connect(self.update_event_duration)
        self.event_end_input.editingFinished.connect(self.update_event_duration)

    def parse_time(self, time_str: str):
        try:
            t = time_str.strip().lower().replace(" ", "")
            if t.endswith("am") or t.endswith("pm"):
                suffix = t[-2:]
                time_part = t[:-2]
            else:
                suffix = None
                time_part = t

            dt = datetime.strptime(time_part, "%H:%M")
            hour = dt.hour
            minute = dt.minute

            if suffix == "pm" and hour < 12:
                hour += 12
            if suffix == "am" and hour == 12:
                hour = 0

            return hour, minute
        except Exception:
            return None

    def update_duration(self):
        start = self.parse_time(self.start_time_input.text())
        end = self.parse_time(self.end_time_input.text())
        if start and end:
            start_minutes = start[0] * 60 + start[1]
            end_minutes = end[0] * 60 + end[1]
            duration = end_minutes - start_minutes
            if duration < 0:
                duration = 0
            self.duration_display.setText(f"{duration} mins")
        else:
            self.duration_display.setText("0 mins")

    def update_event_duration(self):
        start = self.parse_time(self.event_start_input.text())
        end = self.parse_time(self.event_end_input.text())
        if start and end:
            start_minutes = start[0] * 60 + start[1]
            end_minutes = end[0] * 60 + end[1]
            duration = end_minutes - start_minutes
            if duration < 0:
                duration = 0
            self.event_duration_display.setText(f"{duration} minutes")
        else:
            self.event_duration_display.setText("0 minutes")

    def generate_message(self):
        host = self.host_input.text().strip()
        timezone = self.timezone_input.text().strip()
        start_time = self.start_time_input.text().strip()
        end_time = self.end_time_input.text().strip()
        duration = self.duration_display.text()
        attendees = self.attendees_input.value()
        passed = self.passed_input.value()
        failed = self.failed_input.value()
        attendees_list = self.attendees_list_input.toPlainText().strip()
        scheduled = self.scheduled_input.currentText()
        notes = self.notes_input.toPlainText().strip()
        proof = self.proof_input.toPlainText().strip()

        if not host:
            QMessageBox.warning(self, "Input Error", "HOST field cannot be empty.")
            return
        if not timezone:
            QMessageBox.warning(self, "Input Error", "TIMEZONE field cannot be empty.")
            return
        if not start_time or not end_time:
            QMessageBox.warning(self, "Input Error", "START TIME and END TIME must be filled.")
            return

        msg_lines = [
            f"[HOST] @{host}",
            f"[TIMEZONE] {timezone}",
            f"[START TIME] {start_time}",
            f"[END TIME] {end_time}",
            f"[DURATION] {duration}",
            f"[ATTENDEES] {attendees}",
            f"[PASSED] {passed}",
            f"[FAILED] {failed}",
        ]
        if attendees_list:
            msg_lines.append(attendees_list)

        msg_lines.append(f"[SCHEDULED] {scheduled}")

        if notes:
            msg_lines.append(f"[NOTES]{notes}")

        if proof:
            msg_lines.append(f"[PROOF] {proof}")

        self.output_box.setPlainText("\n".join(msg_lines))

    def generate_phase_log(self):
        host = self.phase_host_input.text().strip()
        training = self.training_input.text().strip()
        attendees = self.phase_attendees_input.value()
        passed = self.phase_passed_input.value()
        attendees_list = self.phase_attendees_list_input.toPlainText().strip()
        failed = self.phase_failed_input.value()
        event_start = self.event_start_input.text().strip()
        event_end = self.event_end_input.text().strip()
        event_duration = self.event_duration_display.text()
        notes = self.phase_notes_input.toPlainText().strip()
        ping = self.ping_input.toPlainText().strip()

        if not host:
            QMessageBox.warning(self, "Input Error", "HOST field cannot be empty.")
            return
        if not training:
            QMessageBox.warning(self, "Input Error", "TRAINING field cannot be empty.")
            return
        if not event_start or not event_end:
            QMessageBox.warning(self, "Input Error", "EVENT START TIME and END TIME must be filled.")
            return

        msg_lines = [
            f"[HOST] @{host}",
            f"[TRAINING] {training}",
            f"[ATTENDEES] {attendees}",
            f"[PASSED] {passed}",
        ]

        if attendees_list:
            msg_lines.append(attendees_list)

        msg_lines.append(f"[FAILED] {failed}")
        msg_lines.append(f"[EVENT START TIME] {event_start}")
        msg_lines.append(f"[EVENT END TIME] {event_end}")
        msg_lines.append(f"[EVENT DURATION] {event_duration}")

        if notes:
            msg_lines.append(f"[NOTES] {notes}")

        if ping:
            msg_lines.append(f"[PING] {ping}")

        self.phase_output_box.setPlainText("\n".join(msg_lines))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiscordMessageFormatter()
    window.show()
    sys.exit(app.exec())
