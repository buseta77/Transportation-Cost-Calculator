import sys
import csv
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QSlider, QGridLayout, QScrollArea, QComboBox,\
    QWidget, QFrame, QHBoxLayout, QVBoxLayout, QFormLayout, QDialog, QFileDialog, QPlainTextEdit
from PyQt5.QtGui import QIntValidator
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
import pandas as pd


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.setWindowIcon(QIcon("icons/moving-truck.png"))
        self.setWindowTitle("Flint Hills Moving - Pricing Calculator")
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        self.setStyleSheet("QWidget {"
                           "background-color: rgb(225, 235, 240);}"
                           "QPushButton {"
                           "background-color: rgb(165, 209, 255);"
                           "border: 2px solid rgb(128, 179, 255);"
                           "border-radius: 5px;"
                           "padding: 2px 5px;}"
                           "QPushButton::hover {"
                           "background-color: rgb(128, 179, 255)}"
                           "QScrollArea {border: 2px solid rgb(128, 179, 255);"
                           "border-radius: 5px;"
                           "background-color: rgb(230, 235, 240);}")

        # we define some fixed values below
        self.integer_only = QIntValidator()

        # we define UI elements below
        self.kitchen_tab = QPushButton()
        self.kitchen_tab.clicked.connect(self.get_kitchen_tab)
        self.kitchen_tab.setText("Kitchen")
        self.bedroom_tab = QPushButton()
        self.bedroom_tab.clicked.connect(self.get_bedroom_tab)
        self.bedroom_tab.setText("Bedroom")
        self.living_tab = QPushButton()
        self.living_tab.clicked.connect(self.get_living_tab)
        self.living_tab.setText("Living Room")
        self.outside_tab = QPushButton()
        self.outside_tab.clicked.connect(self.get_outside_tab)
        self.outside_tab.setText("Outside")
        self.office_tab = QPushButton()
        self.office_tab.clicked.connect(self.get_office_tab)
        self.office_tab.setText("Office")
        self.boxes_tab = QPushButton()
        self.boxes_tab.clicked.connect(self.get_boxes_tab)
        self.boxes_tab.setText("Boxes")
        #####
        self.kitchen_scroll_area = QScrollArea()
        self.kitchen_scroll_area.setWidgetResizable(True)
        self.kitchen_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        kitchen_scrollbar = self.kitchen_scroll_area.children()[2]
        kitchen_scrollbar.setStyleSheet("""QScrollBar:vertical {
                                           border-color: rgb(225, 235, 240);
                                           border-width: 1px;
                                           border-style: solid;
                                           border-radius: 10px;
                                           background: rgb(225, 235, 240);
                                           width:18px;
                                           margin: 10px 6px 10px 0;}
                                           QScrollBar::handle:vertical {
                                           background-color: rgb(128, 179, 255);
                                           min-height: 25px;
                                           border: 1px solid rgb(128, 179, 255);
                                           border-radius: 5px;}
                                           QScrollBar::add-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(239, 229, 220);
                                           height: 0px;
                                           subcontrol-position: bottom;
                                           subcontrol-origin: margin;}
                                           QScrollBar::sub-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(241, 241, 241);
                                           height: 0px;
                                           subcontrol-position: top;
                                           subcontrol-origin: margin;}
                                           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                           background: none;}""")
        self.kitchen_widget = QWidget()
        self.kitchen_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.kitchen_widget_layout = QFormLayout()
        self.kitchen_widget.setLayout(self.kitchen_widget_layout)
        self.kitchen_scroll_area.setWidget(self.kitchen_widget)
        self.bedroom_scroll_area = QScrollArea()
        self.bedroom_scroll_area.setWidgetResizable(True)
        self.bedroom_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        bedroom_scrollbar = self.bedroom_scroll_area.children()[2]
        bedroom_scrollbar.setStyleSheet("""QScrollBar:vertical {              
                                           border-color: rgb(225, 235, 240);
                                           border-width: 1px;
                                           border-style: solid;
                                           border-radius: 10px;
                                           background: rgb(225, 235, 240);
                                           width:18px;
                                           margin: 10px 6px 10px 0;}
                                           QScrollBar::handle:vertical {
                                           background-color: rgb(128, 179, 255);
                                           min-height: 25px;
                                           border: 1px solid rgb(128, 179, 255);
                                           border-radius: 5px;}
                                           QScrollBar::add-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(239, 229, 220);
                                           height: 0px;
                                           subcontrol-position: bottom;
                                           subcontrol-origin: margin;}
                                           QScrollBar::sub-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(241, 241, 241);
                                           height: 0px;
                                           subcontrol-position: top;
                                           subcontrol-origin: margin;}
                                           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                           background: none;}""")
        self.bedroom_widget = QWidget()
        self.bedroom_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.bedroom_widget_layout = QFormLayout()
        self.bedroom_widget.setLayout(self.bedroom_widget_layout)
        self.bedroom_scroll_area.setWidget(self.bedroom_widget)
        self.living_scroll_area = QScrollArea()
        self.living_scroll_area.setWidgetResizable(True)
        self.living_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        living_scrollbar = self.living_scroll_area.children()[2]
        living_scrollbar.setStyleSheet("""QScrollBar:vertical {              
                                       border-color: rgb(225, 235, 240);
                                       border-width: 1px;
                                       border-style: solid;
                                       border-radius: 10px;
                                       background: rgb(225, 235, 240);
                                       width:18px;
                                       margin: 10px 6px 10px 0;}
                                       QScrollBar::handle:vertical {
                                       background-color: rgb(128, 179, 255);
                                       min-height: 25px;
                                       border: 1px solid rgb(128, 179, 255);
                                       border-radius: 5px;}
                                       QScrollBar::add-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(239, 229, 220);
                                       height: 0px;
                                       subcontrol-position: bottom;
                                       subcontrol-origin: margin;}
                                       QScrollBar::sub-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(241, 241, 241);
                                       height: 0px;
                                       subcontrol-position: top;
                                       subcontrol-origin: margin;}
                                       QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                       background: none;}""")
        self.living_widget = QWidget()
        self.living_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.living_widget_layout = QFormLayout()
        self.living_widget.setLayout(self.living_widget_layout)
        self.living_scroll_area.setWidget(self.living_widget)
        self.outside_scroll_area = QScrollArea()
        self.outside_scroll_area.setWidgetResizable(True)
        self.outside_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        outside_scrollbar = self.outside_scroll_area.children()[2]
        outside_scrollbar.setStyleSheet("""QScrollBar:vertical {              
                                           border-color: rgb(225, 235, 240);
                                           border-width: 1px;
                                           border-style: solid;
                                           border-radius: 10px;
                                           background: rgb(225, 235, 240);
                                           width:18px;
                                           margin: 10px 6px 10px 0;}
                                           QScrollBar::handle:vertical {
                                           background-color: rgb(128, 179, 255);
                                           min-height: 25px;
                                           border: 1px solid rgb(128, 179, 255);
                                           border-radius: 5px;}
                                           QScrollBar::add-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(239, 229, 220);
                                           height: 0px;
                                           subcontrol-position: bottom;
                                           subcontrol-origin: margin;}
                                           QScrollBar::sub-line:vertical {
                                           border: 1px solid rgb(239, 229, 220);
                                           background-color: rgb(241, 241, 241);
                                           height: 0px;
                                           subcontrol-position: top;
                                           subcontrol-origin: margin;}
                                           QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                           background: none;}""")
        self.outside_widget = QWidget()
        self.outside_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.outside_widget_layout = QFormLayout()
        self.outside_widget.setLayout(self.outside_widget_layout)
        self.outside_scroll_area.setWidget(self.outside_widget)
        self.office_scroll_area = QScrollArea()
        self.office_scroll_area.setWidgetResizable(True)
        self.office_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        office_scrollbar = self.office_scroll_area.children()[2]
        office_scrollbar.setStyleSheet("""QScrollBar:vertical {              
                                       border-color: rgb(225, 235, 240);
                                       border-width: 1px;
                                       border-style: solid;
                                       border-radius: 10px;
                                       background: rgb(225, 235, 240);
                                       width:18px;
                                       margin: 10px 6px 10px 0;}
                                       QScrollBar::handle:vertical {
                                       background-color: rgb(128, 179, 255);
                                       min-height: 25px;
                                       border: 1px solid rgb(128, 179, 255);
                                       border-radius: 5px;}
                                       QScrollBar::add-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(239, 229, 220);
                                       height: 0px;
                                       subcontrol-position: bottom;
                                       subcontrol-origin: margin;}
                                       QScrollBar::sub-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(241, 241, 241);
                                       height: 0px;
                                       subcontrol-position: top;
                                       subcontrol-origin: margin;}
                                       QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                       background: none;}""")
        self.office_widget = QWidget()
        self.office_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.office_widget_layout = QFormLayout()
        self.office_widget.setLayout(self.office_widget_layout)
        self.office_scroll_area.setWidget(self.office_widget)
        self.boxes_scroll_area = QScrollArea()
        self.boxes_scroll_area.setWidgetResizable(True)
        self.boxes_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxes_scrollbar = self.boxes_scroll_area.children()[2]
        boxes_scrollbar.setStyleSheet("""QScrollBar:vertical {              
                                       border-color: rgb(225, 235, 240);
                                       border-width: 1px;
                                       border-style: solid;
                                       border-radius: 10px;
                                       background: rgb(225, 235, 240);
                                       width:18px;
                                       margin: 10px 6px 10px 0;}
                                       QScrollBar::handle:vertical {
                                       background-color: rgb(128, 179, 255);
                                       min-height: 25px;
                                       border: 1px solid rgb(128, 179, 255);
                                       border-radius: 5px;}
                                       QScrollBar::add-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(239, 229, 220);
                                       height: 0px;
                                       subcontrol-position: bottom;
                                       subcontrol-origin: margin;}
                                       QScrollBar::sub-line:vertical {
                                       border: 1px solid rgb(239, 229, 220);
                                       background-color: rgb(241, 241, 241);
                                       height: 0px;
                                       subcontrol-position: top;
                                       subcontrol-origin: margin;}
                                       QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                                       background: none;}""")
        self.boxes_widget = QWidget()
        self.boxes_widget.setStyleSheet(
                           "border: 0px;"
                           "border-radius: 5px;"
                           "background-color: rgb(225, 235, 240);")
        self.boxes_widget_layout = QFormLayout()
        self.boxes_widget.setLayout(self.boxes_widget_layout)
        self.boxes_scroll_area.setWidget(self.boxes_widget)
        #####
        self.clear_selections_button = QPushButton()
        self.clear_selections_button.clicked.connect(self.clear_selections)
        self.clear_selections_button.setText("Clear")
        self.edit_items_button = QPushButton()
        self.edit_items_button.clicked.connect(self.edit_items)
        self.edit_items_button.setText("Edit Items")
        self.edit_formulas_button = QPushButton()
        self.edit_formulas_button.clicked.connect(self.edit_formulas)
        self.edit_formulas_button.setText("Edit Formulas")
        self.edit_value_multiplier_button = QPushButton()
        self.edit_value_multiplier_button.clicked.connect(self.edit_hidden_values)
        self.edit_value_multiplier_button.setText(" Edit Item Value ")
        self.import_button = QPushButton()
        self.import_button.setText("Import")
        self.import_button.clicked.connect(self.import_list)
        #####
        self.round_trip_distance_label = QLabel()
        self.round_trip_distance_label.setText("Round Trip Distance:")
        self.round_trip_distance = QLineEdit()
        self.round_trip_distance.setStyleSheet("border: 1px solid rgb(128, 179, 255);"
                                               "border-radius: 3px;"
                                               "background-color: rgb(250, 250, 250);")
        self.round_trip_distance.setValidator(self.integer_only)
        self.round_trip_distance.setText("0")
        self.round_trip_distance.setFixedWidth(70)
        self.estimator_adjustment_label = QLabel()
        self.estimator_adjustment_label.setText("Estimator Adjustment:")
        self.estimator_adjustment = QLineEdit()
        self.estimator_adjustment.setStyleSheet("border: 1px solid rgb(128, 179, 255);"
                                                "border-radius: 3px;"
                                                "background-color: rgb(250, 250, 250);")
        self.estimator_adjustment.setValidator(self.integer_only)
        self.estimator_adjustment.setText("0")
        self.estimator_adjustment.setFixedWidth(70)
        self.ft_riley_adjustment_label = QLabel()
        self.ft_riley_adjustment_label.setText("Fort Riley Adjustment:")
        self.ft_riley_adjustment = QComboBox()
        self.ft_riley_adjustment.setStyleSheet("QComboBox {border: 1px solid rgb(128, 179, 255);"
                                               "border-radius: 3px;"
                                               "background-color: rgb(250, 250, 250);}"
                                               "QComboBox::drop-down {"
                                               "background-color: rgb(250, 250, 250);"
                                               "border-radius: 3px;}"
                                               "QComboBox::down-arrow {"
                                               "image: url(icons/arrow.png);"
                                               "width: 8px;"
                                               "height: 8px;}"
                                               "QComboBox QAbstractItemView {"
                                               "background-color: rgb(250, 250, 250);}")
        self.ft_riley_adjustment.addItem("No")
        self.ft_riley_adjustment.addItem("Yes")
        self.ft_riley_adjustment.setFixedWidth(70)
        self.slider_frame = QFrame()
        self.slider_layout = QVBoxLayout()
        self.slider_frame.setLayout(self.slider_layout)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 5)
        self.slider.setPageStep(1)
        self.slider.valueChanged.connect(self.change_slider_label)
        self.slider.setStyleSheet("QSlider::handle:horizontal {"
                                  "background-color: rgb(165, 209, 255);"
                                  "border: 2px solid rgb(128, 179, 255);"
                                  "border-radius: 5px;}"
                                  "QSlider::handle:horizontal:hover {"
                                  "background-color: rgb(128, 179, 255);}")
        self.slider_label = QLabel()
        self.slider.setValue(3)
        self.slider.setMinimumWidth(260)
        self.slider_layout.addWidget(self.slider, alignment=Qt.AlignBottom)
        self.slider_layout.addWidget(self.slider_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.calculate_estimate_button = QPushButton()
        self.calculate_estimate_button.clicked.connect(self.calculate_estimate)
        self.calculate_estimate_button.setText("Calculate")
        self.calculate_estimate_button.setStyleSheet("QPushButton {background-color: rgb(255, 179, 102);"
                                                     "border: 2px solid rgb(255, 128, 0);"
                                                     "border-radius: 5px;"
                                                     "padding: 5px 5px;}"
                                                     "QPushButton::hover {background-color: rgb(255, 128, 0);}")
        self.main_estimate_label = QLabel()
        self.unload_only_estimate_label = QLabel()
        self.load_only_estimate_label = QLabel()
        self.see_details_button = QPushButton()
        self.see_details_button.setText("See Details")
        self.see_details_button.setStyleSheet("QPushButton {background-color: rgb(255, 179, 102);"
                                              "border: 2px solid rgb(255, 128, 0);"
                                              "border-radius: 5px;"
                                              "padding: 2px 5px;}"
                                              "QPushButton::hover {background-color: rgb(255, 128, 0);}")
        self.export_list_button = QPushButton()
        self.export_list_button.setText("Export")
        self.export_list_button.setStyleSheet("QPushButton {background-color: rgb(255, 179, 102);"
                                              "border: 2px solid rgb(255, 128, 0);"
                                              "border-radius: 5px;"
                                              "padding: 2px 5px;}"
                                              "QPushButton::hover {background-color: rgb(255, 128, 0);}")
        self.details_frame = QFrame()
        self.details_layout = QFormLayout()
        self.details_frame.setLayout(self.details_layout)
        self.details_frame.setStyleSheet("QFrame {border: 2px solid rgb(128, 179, 255);"
                                         "border-radius: 5px;}"
                                         "QLabel {border:none;}")
        self.details_1 = QLabel()
        self.details_2 = QLabel()
        self.details_3 = QLabel()
        self.details_4 = QLabel()
        self.details_5 = QLabel()
        self.details_6 = QLabel()
        self.details_7 = QLabel()
        self.details_8 = QLabel()
        self.details_9 = QLabel()
        self.details_10 = QLabel()
        self.details_11 = QLabel()
        self.details_12 = QLabel()
        self.details_layout.addWidget(self.details_1)
        self.details_layout.addWidget(self.details_2)
        self.details_layout.addWidget(self.details_3)
        self.details_layout.addWidget(self.details_4)
        self.details_layout.addWidget(self.details_5)
        self.details_layout.addWidget(self.details_6)
        self.details_layout.addWidget(self.details_7)
        self.details_layout.addWidget(self.details_8)
        self.details_layout.addWidget(self.details_9)
        self.details_layout.addWidget(self.details_10)
        self.details_layout.addWidget(self.details_11)
        self.details_layout.addWidget(self.details_12)
        self.details_frame.hide()

        # we place defined UI elements to the GUI below
        self.main_layout.setRowMinimumHeight(0, 10)
        self.main_layout.setColumnMinimumWidth(0, 30)
        self.main_layout.setColumnMinimumWidth(7, 30)
        self.main_layout.setColumnMinimumWidth(11, 30)
        self.main_layout.setRowMinimumHeight(23, 10)
        self.main_layout.setColumnMinimumWidth(8, 80)
        self.main_layout.setColumnMinimumWidth(9, 80)
        self.main_layout.setColumnMinimumWidth(10, 80)
        self.main_layout.addWidget(self.kitchen_tab, 1, 1, 1, 1)
        self.main_layout.addWidget(self.bedroom_tab, 1, 2, 1, 1)
        self.main_layout.addWidget(self.living_tab, 1, 3, 1, 1)
        self.main_layout.addWidget(self.outside_tab, 1, 4, 1, 1)
        self.main_layout.addWidget(self.office_tab, 1, 5, 1, 1)
        self.main_layout.addWidget(self.boxes_tab, 1, 6, 1, 1)
        self.main_layout.addWidget(self.kitchen_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.bedroom_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.living_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.outside_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.office_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.boxes_scroll_area, 2, 1, 20, 6)
        self.main_layout.addWidget(self.clear_selections_button, 22, 6, 1, 1, alignment=Qt.AlignRight)
        self.main_layout.addWidget(self.edit_items_button, 22, 1, 1, 1)
        self.main_layout.addWidget(self.edit_formulas_button, 22, 2, 1, 1)
        self.main_layout.addWidget(self.edit_value_multiplier_button, 22, 3, 1, 1)
        self.main_layout.addWidget(self.import_button, 22, 4, 1, 1)
        self.main_layout.addWidget(self.round_trip_distance_label, 2, 8, 1, 2)
        self.main_layout.addWidget(self.round_trip_distance,  2, 10, 1, 1, alignment=Qt.AlignRight)
        self.main_layout.addWidget(self.estimator_adjustment_label, 3, 8, 1, 2)
        self.main_layout.addWidget(self.estimator_adjustment, 3, 10, 1, 1, alignment=Qt.AlignRight)
        self.main_layout.addWidget(self.ft_riley_adjustment_label, 4, 8, 1, 2)
        self.main_layout.addWidget(self.ft_riley_adjustment, 4, 10, 1, 1, alignment=Qt.AlignRight)
        self.main_layout.addWidget(self.slider_frame, 5, 8, 2, 3, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.calculate_estimate_button, 7, 8, 1, 3, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.main_estimate_label, 8, 8, 1, 3, alignment=Qt.AlignBottom)
        self.main_layout.addWidget(self.unload_only_estimate_label, 9, 8, 1, 3)
        self.main_layout.addWidget(self.load_only_estimate_label, 10, 8, 1, 3, alignment=Qt.AlignTop)
        self.main_layout.addWidget(self.see_details_button, 22, 8, 1, 2, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.details_frame, 11, 8, 11, 3, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.export_list_button, 22, 9, 1, 2, alignment=Qt.AlignRight)

        # we set initial properties below
        self.i_kitchen = 0
        self.i_bedroom = 0
        self.i_living = 0
        self.i_outside = 0
        self.i_office = 0
        self.i_boxes = 0
        self.i_total = 0
        self.see_details_button.hide()
        self.export_list_button.hide()
        self.get_kitchen_tab()
        self.import_note = ''

        # set font size below
        for label in self.findChildren(QLabel):
            label.setFont(QFont('Times', 10))
        for lineedit in self.findChildren(QLineEdit):
            lineedit.setFont(QFont('Times', 10))
        for button in self.findChildren(QPushButton):
            button.setFont(QFont('Times', 9))
        for combobox in self.findChildren(QComboBox):
            combobox.setFont(QFont('Times', 10))
        for item in self.details_frame.findChildren(QLabel):
            item.setFont(QFont('Times', 9))

        # pull info from database and put into app below
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT item_name, hidden_value, item_tab FROM items'''
        cursor.execute(sql)
        # item list will hold all data of items inside a list
        self.all_items = cursor.fetchall()
        self.formula_numbers = []
        conn.close()
        for item in self.all_items:
            if item[2] == 'Kitchen':
                self.add_row(self.kitchen_widget_layout, item[0], item[2])
            elif item[2] == 'Bedroom':
                self.add_row(self.bedroom_widget_layout, item[0], item[2])
            elif item[2] == 'Living Room':
                self.add_row(self.living_widget_layout, item[0], item[2])
            elif item[2] == 'Outside':
                self.add_row(self.outside_widget_layout, item[0], item[2])
            elif item[2] == 'Office':
                self.add_row(self.office_widget_layout, item[0], item[2])
            elif item[2] == 'Boxes':
                self.add_row(self.boxes_widget_layout, item[0], item[2])

        # adjust minimum scrollable area width below
        row_button_width = self.outside_scroll_area.findChild(QPushButton).width()
        row_line_edit_width = self.outside_scroll_area.findChild(QLineEdit).width()
        label_width = []
        for label in self.kitchen_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        for label in self.bedroom_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        for label in self.living_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        for label in self.boxes_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        for label in self.office_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        for label in self.outside_scroll_area.findChildren(QLabel):
            label.adjustSize()
            label_width.append(label.width())
        row_height = self.outside_scroll_area.findChild(QFrame).height() * 10
        min_scroll_width = max(label_width) + row_button_width + row_button_width + row_line_edit_width + 20
        self.kitchen_scroll_area.setMinimumSize(min_scroll_width, row_height)
        self.bedroom_scroll_area.setMinimumSize(min_scroll_width, row_height)
        self.living_scroll_area.setMinimumSize(min_scroll_width, row_height)
        self.boxes_scroll_area.setMinimumSize(min_scroll_width, row_height)
        self.office_scroll_area.setMinimumSize(min_scroll_width, row_height)
        self.outside_scroll_area.setMinimumSize(min_scroll_width, row_height)

        # set initial size
        width = self.width()
        self.resize(800, width)

    def get_kitchen_tab(self):
        self.kitchen_scroll_area.show()
        self.bedroom_scroll_area.hide()
        self.living_scroll_area.hide()
        self.boxes_scroll_area.hide()
        self.office_scroll_area.hide()
        self.outside_scroll_area.hide()
        self.kitchen_tab.setStyleSheet("color: rgb(179, 89, 0);")
        self.bedroom_tab.setStyleSheet("color: black;")
        self.boxes_tab.setStyleSheet("color: black;")
        self.office_tab.setStyleSheet("color: black;")
        self.living_tab.setStyleSheet("color: black;")
        self.outside_tab.setStyleSheet("color: black;")

    def get_bedroom_tab(self):
        self.kitchen_scroll_area.hide()
        self.bedroom_scroll_area.show()
        self.living_scroll_area.hide()
        self.boxes_scroll_area.hide()
        self.office_scroll_area.hide()
        self.outside_scroll_area.hide()
        self.kitchen_tab.setStyleSheet("color: black;")
        self.bedroom_tab.setStyleSheet("color: rgb(179, 89, 0);")
        self.boxes_tab.setStyleSheet("color: black;")
        self.office_tab.setStyleSheet("color: black;")
        self.living_tab.setStyleSheet("color: black;")
        self.outside_tab.setStyleSheet("color: black;")

    def get_living_tab(self):
        self.kitchen_scroll_area.hide()
        self.bedroom_scroll_area.hide()
        self.living_scroll_area.show()
        self.boxes_scroll_area.hide()
        self.office_scroll_area.hide()
        self.outside_scroll_area.hide()
        self.kitchen_tab.setStyleSheet("color: black;")
        self.bedroom_tab.setStyleSheet("color: black;")
        self.boxes_tab.setStyleSheet("color: black;")
        self.office_tab.setStyleSheet("color: black;")
        self.living_tab.setStyleSheet("color: rgb(179, 89, 0);")
        self.outside_tab.setStyleSheet("color: black;")

    def get_outside_tab(self):
        self.kitchen_scroll_area.hide()
        self.bedroom_scroll_area.hide()
        self.living_scroll_area.hide()
        self.boxes_scroll_area.hide()
        self.office_scroll_area.hide()
        self.outside_scroll_area.show()
        self.kitchen_tab.setStyleSheet("color: black;")
        self.bedroom_tab.setStyleSheet("color: black;")
        self.boxes_tab.setStyleSheet("color: black;")
        self.office_tab.setStyleSheet("color: black;")
        self.living_tab.setStyleSheet("color: black;")
        self.outside_tab.setStyleSheet("color: rgb(179, 89, 0);")

    def get_office_tab(self):
        self.kitchen_scroll_area.hide()
        self.bedroom_scroll_area.hide()
        self.living_scroll_area.hide()
        self.boxes_scroll_area.hide()
        self.office_scroll_area.show()
        self.outside_scroll_area.hide()
        self.kitchen_tab.setStyleSheet("color: black;")
        self.bedroom_tab.setStyleSheet("color: black;")
        self.boxes_tab.setStyleSheet("color: black;")
        self.office_tab.setStyleSheet("color: rgb(179, 89, 0);")
        self.living_tab.setStyleSheet("color: black;")
        self.outside_tab.setStyleSheet("color: black;")

    def get_boxes_tab(self):
        self.kitchen_scroll_area.hide()
        self.bedroom_scroll_area.hide()
        self.living_scroll_area.hide()
        self.boxes_scroll_area.show()
        self.office_scroll_area.hide()
        self.outside_scroll_area.hide()
        self.kitchen_tab.setStyleSheet("color: black;")
        self.bedroom_tab.setStyleSheet("color: black;")
        self.boxes_tab.setStyleSheet("color: rgb(179, 89, 0);")
        self.office_tab.setStyleSheet("color: black;")
        self.living_tab.setStyleSheet("color: black;")
        self.outside_tab.setStyleSheet("color: black;")

    def change_slider_label(self):
        current_value = self.slider.value()
        if current_value == 1:
            self.slider_label.setText("Low Range Value")
        elif current_value == 2:
            self.slider_label.setText("Low-Medium Range Value")
        elif current_value == 3:
            self.slider_label.setText("Estimate Amount")
        elif current_value == 4:
            self.slider_label.setText("Medium-High Range Value")
        else:
            self.slider_label.setText("High Range Value")

    def add_row(self, widget_layout, name, tab):
        row_frame = QFrame(self)
        row_frame.setStyleSheet("border: 1px solid rgb(128, 179, 255);"
                                "border-radius: 3px;")
        row_layout = QHBoxLayout()
        row_layout.setSpacing(10)
        row_frame.setLayout(row_layout)
        item_name = QLabel(row_frame)
        item_name.setStyleSheet("border: none;")
        item_name.setText(f"{name}")
        minus_button = QPushButton(row_frame)
        minus_button.setStyleSheet("border: none; margin: 3px;")
        minus_button.setIcon(QIcon("icons/minus.png"))
        number_of_item = QLineEdit(row_frame)
        number_of_item.setStyleSheet("background-color: rgb(250, 250, 250);")
        number_of_item.setValidator(self.integer_only)
        number_of_item.setText("0")
        number_of_item.setFixedWidth(40)
        plus_button = QPushButton(row_frame)
        plus_button.setStyleSheet("border: none; margin: 3px;")
        plus_button.setIcon(QIcon("icons/plus.png"))
        #####
        minus_button.clicked.connect(self.minus_number)
        plus_button.clicked.connect(self.plus_number)

        # add row elements below
        row_layout.addWidget(item_name, alignment=Qt.AlignLeft)
        row_layout.addStretch()
        row_layout.addWidget(minus_button, alignment=Qt.AlignRight)
        row_layout.addWidget(number_of_item)
        row_layout.addWidget(plus_button, alignment=Qt.AlignLeft)
        widget_layout.addWidget(row_frame)
        for label in row_frame.findChildren(QLabel):
            label.setFont(QFont('Times', 10))
        for lineedit in row_frame.findChildren(QLineEdit):
            lineedit.setFont(QFont('Times', 10))
        if tab == 'Kitchen':
            self.i_kitchen += 1
        elif tab == 'Bedroom':
            self.i_bedroom += 1
        elif tab == 'Living Room':
            self.i_living += 1
        elif tab == 'Outside':
            self.i_outside += 1
        elif tab == 'Office':
            self.i_office += 1
        elif tab == 'Boxes':
            self.i_boxes += 1
        self.i_total += 1

    def minus_number(self):
        sender = self.sender()
        parent = sender.parentWidget()
        line_edit = parent.findChild(QLineEdit)
        try:
            number = int(line_edit.text())
        except ValueError:
            return
        if number > 0:
            number -= 1
        line_edit.setText(str(number))

    def plus_number(self):
        sender = self.sender()
        parent = sender.parentWidget()
        line_edit = parent.findChild(QLineEdit)
        try:
            number = int(line_edit.text())
        except ValueError:
            return
        number += 1
        line_edit.setText(str(number))

    def edit_items(self):

        def change_edited_item():
            name = choose_item_combobox.currentText()
            item_name.setEnabled(True)
            item_value.setEnabled(True)
            item_tab.setEnabled(True)
            save_button.setEnabled(True)
            save_button.setToolTip("Leave item name blank to delete this item")
            if name == "-- Add New Item --":
                item_name.clear()
                item_value.clear()
                item_tab.clear()
                item_tab.setPlaceholderText(" ")
                item_tab.addItem("Kitchen")
                item_tab.addItem("Bedroom")
                item_tab.addItem("Living Room")
                item_tab.addItem("Outside")
                item_tab.addItem("Office")
                item_tab.addItem("Boxes")
            else:
                for item in self.all_items:
                    if item[0] == name:
                        item_name.setText(str(item[0]))
                        item_value.setText(str(item[1]))
                        item_tab.setCurrentText(item[2])

        self.edit_items_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.edit_items_window.setWindowIcon(QIcon("icons/edit.png"))
        layout = QGridLayout()
        self.edit_items_window.setLayout(layout)
        self.edit_items_window.setWindowTitle("Edit Items")
        self.edit_items_window.setStyleSheet("QDialog {"
                                             "background-color: rgb(225, 235, 240);}"
                                             "QPushButton {"
                                             "background-color: rgb(165, 209, 255);"
                                             "border: 2px solid rgb(128, 179, 255);"
                                             "border-radius: 5px;"
                                             "padding: 2px 5px;}"
                                             "QPushButton::hover {"
                                             "background-color: rgb(128, 179, 255);}"
                                             "QLineEdit {"
                                             "border: 1px solid rgb(128, 179, 255);"
                                             "border-radius: 3px;"
                                             "background-color: rgb(250, 250, 250);"
                                             "padding: 2px 2px;}"
                                             "QComboBox {border: 1px solid rgb(128, 179, 255);"
                                             "border-radius: 3px;"
                                             "background-color: rgb(250, 250, 250);"
                                             "padding: 2px 2px;}"
                                             "QComboBox::drop-down {"
                                             "background-color: rgb(250, 250, 250);"
                                             "border-radius: 3px;}"
                                             "QComboBox::down-arrow {"
                                             "image: url(icons/arrow.png);"
                                             "width: 8px;"
                                             "height: 8px;}"
                                             "QComboBox QAbstractItemView {"
                                             "background-color: rgb(250, 250, 250);}")
        edit_items_widget = QWidget(self.edit_items_window)
        layout.addWidget(edit_items_widget)
        edit_items_layout = QGridLayout()
        edit_items_widget.setLayout(edit_items_layout)
        # get latest info from database below
        self.all_items.clear()
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT item_name, hidden_value, item_tab FROM items'''
        cursor.execute(sql)
        self.all_items = cursor.fetchall()
        conn.close()
        # define UI elements below
        choose_item_combobox = QComboBox()
        choose_item_combobox.setPlaceholderText(" ")
        choose_item_combobox.addItem("-- Add New Item --")
        for item in self.all_items:
            choose_item_combobox.addItem(item[0])
        choose_item_combobox.currentTextChanged.connect(change_edited_item)
        item_name_label = QLabel()
        item_name_label.setText("Item Name:")
        item_name = QLineEdit()
        item_name.setEnabled(False)
        item_value_label = QLabel()
        item_value_label.setText("Item Hidden Value:")
        item_value = QLineEdit()
        item_value.setEnabled(False)
        item_tab_label = QLabel()
        item_tab_label.setText("Item Tab:")
        item_tab = QComboBox()
        item_tab.setEnabled(False)
        item_tab.setPlaceholderText(" ")
        item_tab.addItem("Kitchen")
        item_tab.addItem("Bedroom")
        item_tab.addItem("Living Room")
        item_tab.addItem("Outside")
        item_tab.addItem("Office")
        item_tab.addItem("Boxes")
        save_button = QPushButton()
        save_button.clicked.connect(lambda: self.save_item(item_name.text(), item_value.text(), item_tab.currentText(),
                                                           choose_item_combobox.currentText()))
        save_button.setText("Save")
        save_button.setEnabled(False)
        # place elements to window below
        edit_items_layout.addWidget(choose_item_combobox, 0, 0, 1, 2)
        edit_items_layout.addWidget(item_name_label, 1, 0, 1, 1)
        edit_items_layout.addWidget(item_name, 1, 1, 1, 1)
        edit_items_layout.addWidget(item_value_label, 2, 0, 1, 1)
        edit_items_layout.addWidget(item_value, 2, 1, 1, 1)
        edit_items_layout.addWidget(item_tab_label, 3, 0, 1, 1)
        edit_items_layout.addWidget(item_tab, 3, 1, 1, 1)
        edit_items_layout.addWidget(save_button, 4, 1, 1, 1)
        for item in self.edit_items_window.findChildren(QLabel):
            item.setFont(QFont('Times', 10))
        for item in self.edit_items_window.findChildren(QComboBox):
            item.setFont(QFont('Times', 9))
        for item in self.edit_items_window.findChildren(QLineEdit):
            item.setFont(QFont('Times', 9))
        for item in self.edit_items_window.findChildren(QPushButton):
            item.setFont(QFont('Times', 9))
        self.edit_items_window.show()

    def save_item(self, name, value, tab, where):
        if value == '':
            return
        if where == "-- Add New Item --":
            conn = sqlite3.connect('items_database.db')
            cursor = conn.cursor()
            sql = f'''INSERT INTO items VALUES
            ('{name}', '{value}', '{tab}')
            '''
            cursor.execute(sql)
            self.all_items = []
            self.all_items = cursor.fetchall()
            conn.commit()
            conn.close()
        else:
            if name == '':
                conn = sqlite3.connect('items_database.db')
                cursor = conn.cursor()
                sql = f'''DELETE FROM items WHERE item_name = '{where}'
                '''
                cursor.execute(sql)
                conn.commit()
                conn.close()
            else:
                conn = sqlite3.connect('items_database.db')
                cursor = conn.cursor()
                sql = f'''UPDATE items SET
                item_name = '{name}',
                hidden_value = '{value}',
                item_tab = '{tab}' WHERE item_name = '{where}'
                '''
                cursor.execute(sql)
                conn.commit()
                conn.close()
        while self.i_kitchen > 0:
            self.kitchen_widget_layout.removeRow(0)
            self.i_kitchen -= 1
        while self.i_bedroom > 0:
            self.bedroom_widget_layout.removeRow(0)
            self.i_bedroom -= 1
        while self.i_office > 0:
            self.office_widget_layout.removeRow(0)
            self.i_office -= 1
        while self.i_living > 0:
            self.living_widget_layout.removeRow(0)
            self.i_living -= 1
        while self.i_outside > 0:
            self.outside_widget_layout.removeRow(0)
            self.i_outside -= 1
        while self.i_boxes > 0:
            self.boxes_widget_layout.removeRow(0)
            self.i_boxes -= 1
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT item_name, hidden_value, item_tab FROM items'''
        cursor.execute(sql)
        # item list will hold all data of items inside a list
        self.all_items = cursor.fetchall()
        conn.close()
        for item in self.all_items:
            if item[2] == 'Kitchen':
                self.add_row(self.kitchen_widget_layout, item[0], item[2])
            elif item[2] == 'Bedroom':
                self.add_row(self.bedroom_widget_layout, item[0], item[2])
            elif item[2] == 'Living Room':
                self.add_row(self.living_widget_layout, item[0], item[2])
            elif item[2] == 'Outside':
                self.add_row(self.outside_widget_layout, item[0], item[2])
            elif item[2] == 'Office':
                self.add_row(self.office_widget_layout, item[0], item[2])
            elif item[2] == 'Boxes':
                self.add_row(self.boxes_widget_layout, item[0], item[2])
        self.edit_items_window.close()

    def edit_formulas(self):

        def change_edited_formula():
            save_button.setEnabled(True)
            formula = choose_item_combobox.currentText().replace(' Formula', '')
            line_1.show()
            line_2.show()
            if formula == 'Distance Addition':
                label_1.setText("If RTD < 30: ")
                line_1.setText(f"{self.formula_numbers[0][0]}")
                label_2.setText("then: RTD * ")
                line_2.setText(f"{self.formula_numbers[0][1]}")
            elif formula == 'Long Distance Addition':
                label_1.setText("If RTD > 500: ")
                line_1.setText(f"{self.formula_numbers[1][0]}")
                label_2.setText("then: ")
                line_2.setText(f"{self.formula_numbers[1][1]}")
            elif formula == 'Fort Riley Adjustment':
                label_1.setText("If YES: ")
                line_1.setText(f"{self.formula_numbers[2][0]}")
                label_2.setText("else: ")
                line_2.setText(f"{self.formula_numbers[2][1]}")
            elif formula == 'Second Truck':
                label_1.setText("If total (with value >= 15) > 30: ")
                line_1.setText(f"{self.formula_numbers[3][0]}")
                label_2.setText("else: ")
                line_2.setText(f"{self.formula_numbers[3][1]}")
            elif formula == 'Small Addition':
                label_1.setText("If total (with value <= 5) > 100: ")
                line_1.setText(f"{self.formula_numbers[4][0]}")
                label_2.setText("else: ")
                line_2.setText(f"{self.formula_numbers[4][1]}")
            elif formula == 'Med Addition':
                label_1.setText("If total (with value between 10-15) > 20: ")
                line_1.setText(f"{self.formula_numbers[5][0]}")
                label_2.setText("else: ")
                line_2.setText(f"{self.formula_numbers[5][1]}")
            elif formula == 'Large Addition':
                label_1.setText("If total (with value >= 20) > 7: ")
                line_1.setText(f"{self.formula_numbers[6][0]}")
                label_2.setText("else: ")
                line_2.setText(f"{self.formula_numbers[6][1]}")
            elif formula == 'Adjust Multiplier':
                label_1.setText("Total * ")
                line_1.setText(f"{self.formula_numbers[7][0]}")
                label_2.setText("")
                line_2.clear()
                line_2.hide()
            elif formula == 'Unload Only':
                label_1.setText("Estimate Amount * ")
                line_1.setText(f"{self.formula_numbers[8][0]}")
                label_2.setText("")
                line_2.clear()
                line_2.hide()
            elif formula == 'Load Only':
                label_1.setText("Estimate Amount * ")
                line_1.setText(f"{self.formula_numbers[9][0]}")
                label_2.setText("")
                line_2.clear()
                line_2.hide()
            elif formula == 'Low Range':
                label_1.setText("Estimate Amount * ")
                line_1.setText(f"{self.formula_numbers[10][0]}")
                label_2.setText("")
                line_2.clear()
                line_2.hide()
            elif formula == 'High Range':
                label_1.setText("Estimate Amount * ")
                line_1.setText(f"{self.formula_numbers[11][0]}")
                label_2.setText("")
                line_2.clear()
                line_2.hide()

        self.edit_formulas_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.edit_formulas_window.setWindowIcon(QIcon("icons/formula.png"))
        layout = QGridLayout()
        self.edit_formulas_window.setLayout(layout)
        self.edit_formulas_window.setWindowTitle("Edit Formulas")
        self.edit_formulas_window.setStyleSheet("QDialog {"
                                                "background-color: rgb(225, 235, 240);}"
                                                "QPushButton {"
                                                "background-color: rgb(165, 209, 255);"
                                                "border: 2px solid rgb(128, 179, 255);"
                                                "border-radius: 5px;"
                                                "padding: 2px 5px;}"
                                                "QPushButton::hover {"
                                                "background-color: rgb(128, 179, 255);}"
                                                "QLineEdit {"
                                                "border: 1px solid rgb(128, 179, 255);"
                                                "border-radius: 3px;"
                                                "background-color: rgb(250, 250, 250);"
                                                "padding: 2px 2px;}"
                                                "QComboBox {border: 1px solid rgb(128, 179, 255);"
                                                "border-radius: 3px;"
                                                "background-color: rgb(250, 250, 250);"
                                                "padding: 2px 2px;}"
                                                "QComboBox::drop-down {"
                                                "background-color: rgb(250, 250, 250);"
                                                "border-radius: 3px;}"
                                                "QComboBox::down-arrow {"
                                                "image: url(icons/arrow.png);"
                                                "width: 8px;"                                                 
                                                "height: 8px;}"
                                                "QComboBox QAbstractItemView {"
                                                "background-color: rgb(250, 250, 250);}")
        edit_formulas_widget = QWidget(self.edit_formulas_window)
        layout.addWidget(edit_formulas_widget)
        edit_formulas_layout = QGridLayout()
        edit_formulas_widget.setLayout(edit_formulas_layout)
        # get latest info from database below
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT formula_name, formula_numbers FROM formulas'''
        cursor.execute(sql)
        self.all_formulas = cursor.fetchall()
        conn.close()
        # define UI elements below
        choose_item_combobox = QComboBox()
        choose_item_combobox.setPlaceholderText(" ")
        self.formula_numbers.clear()
        for item in self.all_formulas:
            if not item[0] == 'Hidden Value Multiplier':
                choose_item_combobox.addItem(f"{item[0]} Formula")
            number = item[1].split("-")
            self.formula_numbers.append(number)
        choose_item_combobox.currentTextChanged.connect(change_edited_formula)
        formula_frame = QFrame()
        frame_layout = QHBoxLayout()
        frame_layout.setSpacing(5)
        formula_frame.setLayout(frame_layout)
        label_1 = QLabel()
        line_1 = QLineEdit()
        line_1.setValidator(self.integer_only)
        line_1.hide()
        label_2 = QLabel()
        line_2 = QLineEdit()
        line_2.setValidator(self.integer_only)
        line_2.hide()
        frame_layout.addWidget(label_1, alignment=Qt.AlignRight)
        frame_layout.addWidget(line_1, alignment=Qt.AlignLeft)
        frame_layout.addWidget(label_2, alignment=Qt.AlignRight)
        frame_layout.addWidget(line_2, alignment=Qt.AlignLeft)
        frame_layout.addStretch()
        save_button = QPushButton()
        save_button.setText("Save")
        save_button.setEnabled(False)
        save_button.setFixedWidth(80)
        save_button.clicked.connect(lambda: self.save_formula(line_1.text(), line_2.text(),
                                                            choose_item_combobox.currentText().replace(' Formula', ''),
                                                              line_2.isVisible()))
        edit_formulas_layout.addWidget(choose_item_combobox, 0, 0, 1, 1)
        edit_formulas_layout.addWidget(formula_frame, 1, 0, 1, 1, alignment=Qt.AlignLeft)
        edit_formulas_layout.addWidget(save_button, 2, 0, 1, 1, alignment=Qt.AlignRight)
        for item in self.edit_formulas_window.findChildren(QLabel):
            item.setFont(QFont('Times', 9))
        for item in self.edit_formulas_window.findChildren(QComboBox):
            item.setFont(QFont('Times', 9))
        for item in self.edit_formulas_window.findChildren(QLineEdit):
            item.setFont(QFont('Times', 9))
        for item in self.edit_formulas_window.findChildren(QPushButton):
            item.setFont(QFont('Times', 9))
        self.edit_formulas_window.show()

    def save_formula(self, value_1, value_2, where, line_2):
        if value_1 == '':
            return
        if not line_2:
            conn = sqlite3.connect('items_database.db')
            cursor = conn.cursor()
            sql = f'''UPDATE formulas SET
                formula_numbers = '{value_1}' WHERE formula_name = '{where}'
                '''
            cursor.execute(sql)
            conn.commit()
            conn.close()
        else:
            if value_2 == '':
                return
            values = [value_1, value_2]
            value = '-'.join(values)
            conn = sqlite3.connect('items_database.db')
            cursor = conn.cursor()
            sql = f'''UPDATE formulas SET
                formula_numbers = '{value}' WHERE formula_name = '{where}'
                '''
            cursor.execute(sql)
            conn.commit()
            conn.close()
        self.edit_formulas_window.close()

    def edit_hidden_values(self):
        self.edit_values_window = QDialog(None, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
        self.edit_values_window.setWindowIcon(QIcon("icons/diamond.png"))
        self.edit_values_window.setWindowTitle("Edit Item Value")
        layout = QGridLayout()
        self.edit_values_window.setLayout(layout)
        self.edit_values_window.setStyleSheet("QDialog {"
                                              "background-color: rgb(225, 235, 240);}"
                                              "QPushButton {"
                                              "background-color: rgb(165, 209, 255);"
                                              "border: 2px solid rgb(128, 179, 255);"
                                              "border-radius: 5px;"
                                              "padding: 2px 5px;}"
                                              "QPushButton::hover {"
                                              "background-color: rgb(128, 179, 255);}"
                                              "QLineEdit {"
                                              "border: 1px solid rgb(128, 179, 255);"
                                              "border-radius: 3px;"
                                              "background-color: rgb(250, 250, 250);"
                                              "padding: 2px 2px;}")
        edit_values_widget = QWidget(self.edit_values_window)
        layout.addWidget(edit_values_widget)
        edit_values_layout = QGridLayout()
        edit_values_widget.setLayout(edit_values_layout)
        # get latest info from database below
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT formula_numbers FROM formulas'''
        cursor.execute(sql)
        hidden_values_raw = cursor.fetchall()[12][0]
        hidden_values = hidden_values_raw.split('-')
        conn.close()
        label_11 = QLabel()
        label_11.setText("If hidden value = ")
        label_21 = QLabel()
        label_21.setText("If hidden value = ")
        label_31 = QLabel()
        label_31.setText("If hidden value = ")
        label_41 = QLabel()
        label_41.setText("If hidden value = ")
        label_51 = QLabel()
        label_51.setText("If hidden value = ")
        label_61 = QLabel()
        label_61.setText("If hidden value = ")
        line_11 = QLineEdit()
        line_11.setText(f"{hidden_values[0]}")
        line_21 = QLineEdit()
        line_21.setText(f"{hidden_values[2]}")
        line_31 = QLineEdit()
        line_31.setText(f"{hidden_values[4]}")
        line_41 = QLineEdit()
        line_41.setText(f"{hidden_values[6]}")
        line_51 = QLineEdit()
        line_51.setText(f"{hidden_values[8]}")
        line_61 = QLineEdit()
        line_61.setText(f"{hidden_values[10]}")
        label_12 = QLabel()
        label_12.setText(", then multiplier =")
        label_22 = QLabel()
        label_22.setText(", then multiplier =")
        label_32 = QLabel()
        label_32.setText(", then multiplier =")
        label_42 = QLabel()
        label_42.setText(", then multiplier =")
        label_52 = QLabel()
        label_52.setText(", then multiplier =")
        label_62 = QLabel()
        label_62.setText(", then multiplier =")
        line_12 = QLineEdit()
        line_12.setText(f"{hidden_values[1]}")
        line_22 = QLineEdit()
        line_22.setText(f"{hidden_values[3]}")
        line_32 = QLineEdit()
        line_32.setText(f"{hidden_values[5]}")
        line_42 = QLineEdit()
        line_42.setText(f"{hidden_values[7]}")
        line_52 = QLineEdit()
        line_52.setText(f"{hidden_values[9]}")
        line_62 = QLineEdit()
        line_62.setText(f"{hidden_values[11]}")
        line_11.setValidator(self.integer_only)
        line_21.setValidator(self.integer_only)
        line_31.setValidator(self.integer_only)
        line_41.setValidator(self.integer_only)
        line_51.setValidator(self.integer_only)
        line_61.setValidator(self.integer_only)
        line_12.setValidator(self.integer_only)
        line_22.setValidator(self.integer_only)
        line_32.setValidator(self.integer_only)
        line_42.setValidator(self.integer_only)
        line_52.setValidator(self.integer_only)
        line_62.setValidator(self.integer_only)
        save_button = QPushButton()
        save_button.clicked.connect(lambda: self.save_value(line_11.text(), line_12.text(), line_21.text(),
                                                            line_22.text(), line_31.text(), line_32.text(),
                                                            line_41.text(), line_42.text(), line_51.text(),
                                                            line_52.text(), line_61.text(), line_62.text()))
        save_button.setText("Save")
        edit_values_layout.addWidget(label_11, 0, 0, 1, 1)
        edit_values_layout.addWidget(label_21, 1, 0, 1, 1)
        edit_values_layout.addWidget(label_31, 2, 0, 1, 1)
        edit_values_layout.addWidget(label_41, 3, 0, 1, 1)
        edit_values_layout.addWidget(label_51, 4, 0, 1, 1)
        edit_values_layout.addWidget(label_61, 5, 0, 1, 1)
        edit_values_layout.addWidget(line_11, 0, 1, 1, 1)
        edit_values_layout.addWidget(line_21, 1, 1, 1, 1)
        edit_values_layout.addWidget(line_31, 2, 1, 1, 1)
        edit_values_layout.addWidget(line_41, 3, 1, 1, 1)
        edit_values_layout.addWidget(line_51, 4, 1, 1, 1)
        edit_values_layout.addWidget(line_61, 5, 1, 1, 1)
        edit_values_layout.addWidget(label_12, 0, 2, 1, 1)
        edit_values_layout.addWidget(label_22, 1, 2, 1, 1)
        edit_values_layout.addWidget(label_32, 2, 2, 1, 1)
        edit_values_layout.addWidget(label_42, 3, 2, 1, 1)
        edit_values_layout.addWidget(label_52, 4, 2, 1, 1)
        edit_values_layout.addWidget(label_62, 5, 2, 1, 1)
        edit_values_layout.addWidget(line_12, 0, 3, 1, 1)
        edit_values_layout.addWidget(line_22, 1, 3, 1, 1)
        edit_values_layout.addWidget(line_32, 2, 3, 1, 1)
        edit_values_layout.addWidget(line_42, 3, 3, 1, 1)
        edit_values_layout.addWidget(line_52, 4, 3, 1, 1)
        edit_values_layout.addWidget(line_62, 5, 3, 1, 1)
        edit_values_layout.addWidget(save_button, 6, 3, 1, 1)
        for item in self.edit_values_window.findChildren(QLabel):
            item.setFont(QFont('Times', 9))
        for item in self.edit_values_window.findChildren(QLineEdit):
            item.setFont(QFont('Times', 9))
        for item in self.edit_values_window.findChildren(QPushButton):
            item.setFont(QFont('Times', 9))
        self.edit_values_window.show()

    def save_value(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11,
                   value12):
        values = [value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12]
        values_raw = '-'.join(values)
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = f'''UPDATE formulas SET
                formula_numbers = '{values_raw}' WHERE formula_name = 'Hidden Value Multiplier'
                '''
        cursor.execute(sql)
        conn.commit()
        conn.close()
        self.edit_values_window.close()

    def import_list(self):
        # read imported csv file below
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose File", "", "CSV Files(*.csv)")
        if file_name:
            self.clear_selections()
            f = pd.read_csv(file_name)
            try:
                rtd_raw = f['DETAILS'][1]
                rtd = str(rtd_raw[rtd_raw.index('RTD=')+len('RTD='):rtd_raw.index('):')])
                fr_raw = f['DETAILS'][3]
                ft = str(fr_raw[fr_raw.index('FRA=')+len('FRA='):fr_raw.index('):')])
                ea_raw = f['DETAILS'][8]
                ea = str(ea_raw[ea_raw.index('EA=')+len('EA='):ea_raw.index('):')])
                scale_raw = f['DETAILS'][12]
                scale = int(scale_raw[scale_raw.index('SCALE=')+len('SCALE='):scale_raw.index('):')])
            except ValueError:
                self.main_estimate_label.setText("Error: Make sure the CSV is in same form as exported one!")
                return
            except KeyError:
                self.main_estimate_label.setText("Error: Make sure headers are 'DETAILS' and 'OUTPUT'!")
                return
            self.round_trip_distance.setText(rtd)
            self.estimator_adjustment.setText(ea)
            self.ft_riley_adjustment.setCurrentText(ft)
            self.slider.setValue(scale)
            no = 16
            # read items and their numbers from csv file below
            items = []
            figure = []
            invalid_item = False
            try:
                while f['DETAILS'][no] != 'NOTE':
                    items.append(f['DETAILS'][no])
                    figure.append(f['OUTPUT'][no])
                    no += 1
            except KeyError:
                self.main_estimate_label.setText("Error: Make sure headers are 'DETAILS' and 'OUTPUT'!")
                return
            while items:
                for x in self.kitchen_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if not items:
                    break
                for x in self.bedroom_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if not items:
                    break
                for x in self.living_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if not items:
                    break
                for x in self.outside_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if not items:
                    break
                for x in self.office_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if not items:
                    break
                for x in self.boxes_scroll_area.findChildren(QLabel):
                    if items[0] == x.text():
                        x.parent().findChildren(QLineEdit)[0].setText(figure[0])
                        items.pop(0)
                        figure.pop(0)
                    if not items:
                        break
                if items:
                    invalid_item = True
                    items.pop(0)
                    figure.pop(0)
                else:
                    break
            if invalid_item:
                self.main_estimate_label.setText("Some items couldn't be imported.")
            else:
                self.main_estimate_label.setText("")
            self.load_only_estimate_label.setText("")
            self.unload_only_estimate_label.setText("")
            self.see_details_button.hide()
            self.details_frame.hide()
            self.export_list_button.hide()
            note_count = 0
            for z in f['DETAILS']:
                if z == 'NOTE':
                    try:
                        self.import_note = str(f['DETAILS'][note_count + 1])
                        break
                    except KeyError:
                        self.import_note = ''
                        break
                else:
                    note_count += 1

    def clear_selections(self):
        for item in self.kitchen_widget.findChildren(QLineEdit):
            item.setText("0")
        for item in self.bedroom_widget.findChildren(QLineEdit):
            item.setText("0")
        for item in self.living_widget.findChildren(QLineEdit):
            item.setText("0")
        for item in self.outside_widget.findChildren(QLineEdit):
            item.setText("0")
        for item in self.boxes_widget.findChildren(QLineEdit):
            item.setText("0")
        for item in self.office_widget.findChildren(QLineEdit):
            item.setText("0")

    def calculate_estimate(self):

        def get_multiplier(value):
            if value == int(hidden_value_formulas[0]):
                return int(hidden_value_formulas[1])
            elif value == int(hidden_value_formulas[2]):
                return int(hidden_value_formulas[3])
            elif value == int(hidden_value_formulas[4]):
                return int(hidden_value_formulas[5])
            elif value == int(hidden_value_formulas[6]):
                return int(hidden_value_formulas[7])
            elif value == int(hidden_value_formulas[8]):
                return int(hidden_value_formulas[9])
            elif value == int(hidden_value_formulas[10]):
                return int(hidden_value_formulas[11])
            else:
                return 1

        def close_details():
            self.see_details_button.setText("See Details")
            self.see_details_button.clicked.disconnect()
            self.see_details_button.clicked.connect(lambda: see_details(base_score, distance_addition,
                                                                        long_distance_addition, fort_riley_addition,
                                                                        second_truck_addition, small_addition,
                                                                        med_addition, large_addition,
                                                                        estimator_addition, adjust, final_value, scale))
            self.details_frame.hide()

        def see_details(base, distance, long_distance, fort_riley, second_truck, small, med, large, estimator, adjust,
                        final, scale):
            sum = base + distance + long_distance + fort_riley + second_truck + small + med + large + estimator
            self.details_1.setText(f"Base Score: ${base}")
            self.details_2.setText(f"Distance Addition: ${distance}")
            self.details_3.setText(f"Long Distance Addition: ${long_distance}")
            self.details_4.setText(f"Fort Riley Addition: ${fort_riley}")
            if second_truck == 2000:
                self.details_5.setText(f"Second Truck: YES (${second_truck})")
            else:
                self.details_5.setText(f"Second Truck: NO (${second_truck})")
            if small > 0:
                self.details_6.setText(f"More Than 100 Small Items: YES (${small})")
            else:
                self.details_6.setText(f"More Than 100 Small Items: NO (${small})")
            if med > 0:
                self.details_7.setText(f"More Than 20 Medium Items: YES (${med})")
            else:
                self.details_7.setText(f"More Than 20 Medium Items: NO (${med})")
            if large > 0:
                self.details_8.setText(f"More Than 7 Large Items: YES (${large})")
            else:
                self.details_8.setText(f"More Than 7 Large Items: NO (${large})")
            self.details_9.setText(f"Estimator Adjustment: ${estimator}")
            self.details_10.setText(f"Sum of Above: ${sum}")
            self.details_11.setText(f"After Adjust Rate ({adjust}): ${'{:.2f}'.format(round(sum * adjust, 2))}")
            self.details_12.setText(f"After Sliding Scale Rate ({scale}): ${'{:.2f}'.format(final)}")
            self.see_details_button.setText("Close Details")
            self.see_details_button.clicked.disconnect()
            self.see_details_button.clicked.connect(close_details)
            self.details_frame.show()

        def open_to_export(items, base, distance, long_distance, fort_riley, second_truck, small, med, large,
                           estimator, adjust, final, scale, unload, load, inputs):
            self.export_window = QDialog(self, Qt.WindowCloseButtonHint | Qt.WindowTitleHint)
            layout = QGridLayout()
            self.export_window.setLayout(layout)
            self.export_window.setWindowTitle("Export List")
            self.export_window.setWindowIcon(QIcon("icons/export.png"))
            self.export_window.setStyleSheet("QDialog {"
                                             "background-color: rgb(225, 235, 240);}"
                                             "QPushButton {"
                                             "background-color: rgb(165, 209, 255);"
                                             "border: 2px solid rgb(128, 179, 255);"
                                             "border-radius: 5px;"
                                             "padding: 2px 10px;"
                                             "margin-top: 5px;}"
                                             "QPushButton::hover {"
                                             "background-color: rgb(128, 179, 255);}"
                                             "QPlainTextEdit {"
                                             "background-color: white;"
                                             "border: 1px solid rgb(128, 179, 255);"
                                             "border-radius: 10px;}")
            export_widget = QWidget(self.export_window)
            layout.addWidget(export_widget)
            export_widget_layout = QGridLayout()
            export_widget.setLayout(export_widget_layout)
            text_area = QPlainTextEdit()
            text_area.setPlaceholderText("Add your note if you wish")
            if self.import_note != '':
                text_area.setPlainText(self.import_note)
            export_button = QPushButton()
            export_button.setText("Export")
            export_button.clicked.connect(lambda: export_to_excel(items, base, distance, long_distance, fort_riley,
                                                                  second_truck, small, med, large,
                                                                  estimator, adjust, final, scale, unload, load,
                                                                  text_area.toPlainText(), self.export_window, inputs))
            error_note = QLabel()
            export_widget_layout.addWidget(text_area, 0, 0, 1, 1)
            export_widget_layout.addWidget(export_button, 1, 0, 1, 1, alignment=Qt.AlignCenter)
            export_widget_layout.addWidget(error_note, 2, 0, 1, 1, alignment=Qt.AlignCenter)
            for item in self.export_window.findChildren(QPushButton):
                item.setFont(QFont('Times', 9))
            for item in self.export_window.findChildren(QPlainTextEdit):
                item.setFont(QFont('Times', 9))
            self.export_window.show()

        def export_to_excel(items, base, distance, long_distance, fort_riley, second_truck, small, med, large,
                            estimator, adjust, final, scale, unload, load, note, window, inputs):
            sum = base + distance + long_distance + fort_riley + second_truck + small + med + large + estimator
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files(*.csv)")
            if file_name:
                try:
                    f = open(file_name, 'w', encoding="utf-8", newline='')
                except PermissionError:
                    window.findChild(QLabel).setText('Error: This file is being used.')
                    return
                writer = csv.writer(f)
                writer.writerow(['DETAILS', 'OUTPUT'])
                writer.writerow(['Base Score:', f'${base}'])
                writer.writerow([f'Distance Addition (RTD={inputs[0]}):', f'${distance}'])
                writer.writerow(['Long Distance Addition:', f'${long_distance}'])
                writer.writerow([f'Fort Riley Addition (FRA={inputs[2]}):', f'${fort_riley}'])
                if second_truck == 2000:
                    writer.writerow(['Second Truck:', f'YES (${second_truck})'])
                else:
                    writer.writerow(['Second Truck:', f'NO (${second_truck})'])
                if small > 0:
                    writer.writerow(['More Than 100 Small Items:', f'YES (${small})'])
                else:
                    writer.writerow(['More Than 100 Small Items:', f'NO (${small})'])
                if med > 0:
                    writer.writerow(['More Than 20 Medium Items:', f'YES (${med})'])
                else:
                    writer.writerow(['More Than 20 Medium Items:', f'NO (${med})'])
                if large > 0:
                    writer.writerow(['More Than 7 Large Items:', f'YES (${large})'])
                else:
                    writer.writerow(['More Than 7 Large Items:', f'NO (${large})'])
                writer.writerow([f'Estimator Adjustment (EA={inputs[1]}):', f'${estimator}'])
                writer.writerow(['Sum of Above:', f'${sum}'])
                writer.writerow([f'After Adjust Rate ({adjust}):', f'${"{:.2f}".format(round(sum * adjust, 2))}'])
                writer.writerow([f'After Sliding Scale Rate ({scale}):', f'${"{:.2f}".format(final)}'])
                writer.writerow([f'Total Estimate (SCALE={inputs[3]}):', f'${"{:.2f}".format(final)}'])
                writer.writerow(['Unload Only Estimate:', f'${"{:.2f}".format(unload)}'])
                writer.writerow(['Load Only Estimate:', f'${"{:.2f}".format(load)}'])
                writer.writerow('')
                writer.writerow(['ITEM NAMES', 'NUMBER'])
                for j in range(len(items)):
                    writer.writerow(items[j])
                writer.writerow('')
                writer.writerow(['NOTE'])
                if note:
                    writer.writerow([note])
                else:
                    writer.writerow('')
                f.close()
                window.close()

        # get latest formulas below
        conn = sqlite3.connect('items_database.db')
        cursor = conn.cursor()
        sql = '''SELECT formula_name, formula_numbers FROM formulas'''
        cursor.execute(sql)
        self.all_formulas = cursor.fetchall()
        conn.close()
        hidden_value_formulas = self.all_formulas[12][1].split('-')
        distance_fee = self.all_formulas[0][1].split('-')
        long_distance_fee = self.all_formulas[1][1].split('-')
        fort_riley_fee = self.all_formulas[2][1].split('-')
        second_truck_fee = self.all_formulas[3][1].split('-')
        small_fee = self.all_formulas[4][1].split('-')
        med_fee = self.all_formulas[5][1].split('-')
        large_fee = self.all_formulas[6][1].split('-')
        adjust = float(self.all_formulas[7][1])
        unload = float(self.all_formulas[8][1])
        load = float(self.all_formulas[9][1])
        low = float(self.all_formulas[10][1])
        low_mid = float((low + 1) / 2)
        high = float(self.all_formulas[11][1])
        high_mid = float((high + 1) / 2)
        slider_value = self.slider.value()

        # prepare values below
        item_list = []
        number_list = []
        value_list = []
        counted_items = []
        base_score = 0
        second_truck_counter = 0
        small_counter = 0
        med_counter = 0
        large_counter = 0

        # get names as a list
        for item in self.kitchen_widget.findChildren(QLabel):
            item_list.append(item.text())
        for item in self.bedroom_widget.findChildren(QLabel):
            item_list.append(item.text())
        for item in self.living_widget.findChildren(QLabel):
            item_list.append(item.text())
        for item in self.outside_widget.findChildren(QLabel):
            item_list.append(item.text())
        for item in self.office_widget.findChildren(QLabel):
            item_list.append(item.text())
        for item in self.boxes_widget.findChildren(QLabel):
            item_list.append(item.text())

        # get numbers as a list
        for item in self.kitchen_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')
        for item in self.bedroom_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')
        for item in self.living_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')
        for item in self.outside_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')
        for item in self.office_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')
        for item in self.boxes_widget.findChildren(QLineEdit):
            if not item.text() == '':
                number_list.append(item.text())
            else:
                number_list.append('0')

        # get values as a list
        for element in item_list:
            for element2 in self.all_items:
                if element == element2[0]:
                    value_list.append(element2[1])

        # make all calculations
        for i in range(len(item_list)):
            if not number_list[i] == '0':
                multiplier = get_multiplier(int(value_list[i]))
                base_score += int(number_list[i]) * int(value_list[i]) * multiplier
                counted_items.append([item_list[i], number_list[i]])
                if int(value_list[i]) >= 15:
                    second_truck_counter += int(number_list[i])
                if int(value_list[i]) <= 5:
                    small_counter += int(number_list[i])
                if int(value_list[i]) >= 10:
                    if int(value_list[i]) <= 15:
                        med_counter += int(number_list[i])
                if int(value_list[i]) >= 20:
                    large_counter += int(number_list[i])
        try:
            if int(self.round_trip_distance.text()) < 30:
                distance_addition = int(distance_fee[0])
            else:
                distance_addition = int(distance_fee[1]) * int(self.round_trip_distance.text())
            if int(self.round_trip_distance.text()) > 500:
                long_distance_addition = int(long_distance_fee[0])
            else:
                long_distance_addition = int(long_distance_fee[1])
            estimator_addition = int(self.estimator_adjustment.text())
        except ValueError:
            self.main_estimate_label.setText("Round trip distance or estimator adjustment is blank!")
            self.load_only_estimate_label.setText("")
            self.unload_only_estimate_label.setText("")
            self.see_details_button.hide()
            self.details_frame.hide()
            self.export_list_button.hide()
            return
        if self.ft_riley_adjustment.currentText() == 'Yes':
            fort_riley_addition = int(fort_riley_fee[0])
        else:
            fort_riley_addition = int(fort_riley_fee[1])
        if second_truck_counter > 30:
            second_truck_addition = int(second_truck_fee[0])
        else:
            second_truck_addition = int(second_truck_fee[1])
        if small_counter > 100:
            small_addition = int(small_fee[0])
        else:
            small_addition = int(small_fee[1])
        if med_counter > 20:
            med_addition = int(med_fee[0])
        else:
            med_addition = int(med_fee[1])
        if large_counter > 7:
            large_addition = int(large_fee[0])
        else:
            large_addition = int(large_fee[1])
        total_before = base_score + distance_addition + long_distance_addition + fort_riley_addition +\
                       second_truck_addition + small_addition + med_addition + large_addition + estimator_addition
        total_estimated = total_before * adjust
        if slider_value == 1:
            final_value = round(total_estimated * low, 2)
            scale = low
        elif slider_value == 2:
            final_value = round(total_estimated * low_mid, 2)
            scale = low_mid
        elif slider_value == 3:
            final_value = round(total_estimated * 1, 2)
            scale = 1
        elif slider_value == 4:
            final_value = round(total_estimated * high_mid, 2)
            scale = high_mid
        else:
            final_value = round(total_estimated * high, 2)
            scale = high
        if final_value == 0:
            self.main_estimate_label.setText("No item entered!")
            self.load_only_estimate_label.setText("")
            self.unload_only_estimate_label.setText("")
            self.see_details_button.hide()
            self.details_frame.hide()
            self.export_list_button.hide()
            return
        load_only_final = round(final_value * load, 2)
        unload_only_final = round(final_value * unload, 2)
        inputs = [int(self.round_trip_distance.text()), estimator_addition, self.ft_riley_adjustment.currentText(),
                  slider_value]
        self.main_estimate_label.setText(f"Estimate: ${'{:.2f}'.format(final_value)}")
        self.unload_only_estimate_label.setText(f"Unload Only Estimate: ${'{:.2f}'.format(unload_only_final)}")
        self.load_only_estimate_label.setText(f"Load Only Estimate: ${'{:.2f}'.format(load_only_final)}")
        self.see_details_button.show()
        self.see_details_button.setText("See Details")
        self.details_frame.hide()
        self.export_list_button.show()
        try:
            self.export_list_button.clicked.disconnect()
        except TypeError:
            pass
        self.export_list_button.clicked.connect(lambda: open_to_export(counted_items, base_score, distance_addition,
                                                                    long_distance_addition, fort_riley_addition,
                                                                    second_truck_addition, small_addition, med_addition,
                                                                    large_addition, estimator_addition, adjust,
                                                                    final_value, scale, unload_only_final,
                                                                    load_only_final, inputs))
        try:
            self.see_details_button.clicked.disconnect()
        except TypeError:
            pass
        self.see_details_button.clicked.connect(lambda: see_details(base_score, distance_addition,
                                                                    long_distance_addition, fort_riley_addition,
                                                                    second_truck_addition, small_addition, med_addition,
                                                                    large_addition, estimator_addition, adjust,
                                                                    final_value, scale))


app = QApplication(sys.argv)
UIWindow = UI()
UIWindow.show()
app.exec_()
