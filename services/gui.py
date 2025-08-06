import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,
    QFileDialog, QComboBox, QHBoxLayout, QSizePolicy, QMessageBox, QTextEdit,
)
from PySide6.QtCore import Qt, QObject, Signal, QMetaObject
from PySide6.QtGui import QTextCursor
class EmittingStream(QObject):
    text_written = Signal(str)

    def write(self, text):
        self.text_written.emit(str(text))

    def flush(self):
        pass

class GUI:
    def __init__(self):
        self.selected_file_path = ""
        self.selected_language = ""
        self._generate_callback = None

        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle("OZI Subtitles Generator")
        self.window.setMinimumSize(800, 300)

        self.layout = QVBoxLayout()

        # Title
        title = QLabel("🎬 OZI Subtitles Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("Select an MP4 file and choose the subtitle language")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px;")
        subtitle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(subtitle)

        self.layout.addSpacing(20)

        # File selection button
        self.file_button = QPushButton("Select MP4 Video")
        self.file_button.clicked.connect(self.select_file)
        self.file_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(self.file_button)

        # Language dropdown
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Subtitle language:")
        lang_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.language_combo = QComboBox()
        self.language_combo.addItems(["pt", "en", "es", "fr"])
        self.language_combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.language_combo)
        self.layout.addLayout(lang_layout)

        self.layout.addStretch()

        # Generate button
        self.generate_button = QPushButton("Generate Now")
        self.generate_button.clicked.connect(self._on_generate_clicked)
        self.generate_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(self.generate_button)

        self.layout.addStretch()

        # Log output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet("font-family: monospace; font-size: 12px; color: white; background-color: black;")
        self.log_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.log_output)

        self.stdout_stream = EmittingStream()
        self.stdout_stream.text_written.connect(self.append_log)
        sys.stdout = self.stdout_stream
        sys.stderr = self.stdout_stream

        # Credits
        credits = QLabel("Created by Jocimar Lopes • Jolo Systems")
        credits.setAlignment(Qt.AlignCenter)
        credits.setStyleSheet("font-size: 11px; color: gray;")
        credits.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout.addWidget(credits)

        self.window.setLayout(self.layout)

    def append_log(self, text):
        self.log_output.moveCursor(QTextCursor.End)
        self.log_output.insertPlainText(text)
        self.log_output.moveCursor(QTextCursor.End)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())
        
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Select MP4 File",
            "",
            "Video Files (*.mp4)"
        )
        if file_path:
            self.file_button.setText(f"Selected: {file_path.split('/')[-1]}")
            self.selected_file_path = file_path
            # Store or handle the selected file path here

    def get_selected_video_and_language(self):
        self.selected_language = self.language_combo.currentText()
        return self.selected_file_path, self.selected_language
    
    def set_generate_callback(self, callback):
        self._generate_callback = callback

    def set_buttons_enabled(self, enabled: bool):
        self.file_button.setEnabled(enabled)
        self.language_combo.setEnabled(enabled)
        self.generate_button.setEnabled(enabled)

    def _on_generate_clicked(self):
        if not self.selected_file_path:
            QMessageBox.warning(self.window, "No file selected", "Please select an MP4 file first.")
            return
        if self._generate_callback:
            self.selected_language = self.language_combo.currentText()
            self.set_buttons_enabled(False)
            self._generate_callback(self.selected_file_path, self.selected_language)
