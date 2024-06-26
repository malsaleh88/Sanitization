# Hackers Poulette™ Contact Form Project

## Overview

This project is a contact form for Hackers Poulette™, a company that sells DIY kits and accessories for Raspberry Pi. The form allows users to contact technical support by filling in their details and sending a message. The project involves server-side sanitization and validation, along with feedback to the user based on their input.

## Features

- **Backend**: Python
  - Introduction to logical structures
  - Sanitization and validation of a form
  - Implementation of POST and GET methods
  - Implementation of templates with Jinja

- **Frontend**:
  - CSS for styling
  - jQuery for client-side validation

## Problem Statement

Hackers Poulette™ wants to enable users to contact their technical support team through a contact form. The mission is to develop a Python script that displays the form and processes its responses, including sanitization, validation, and user feedback.

## Performance Criteria

- **Error Handling**: If the user makes an error, the form should be returned with valid responses preserved in their respective input fields. Error messages should ideally be displayed near the respective fields.
- **Server-side Processing**:
  - Sanitization: Neutralizing any harmful encoding (e.g., `<script>`).
  - Validation: Ensuring all mandatory fields are filled and that the email is valid.
- **Feedback**: If sanitization and validation are successful, a "Thank you for contacting us" page will be displayed, summarizing the encoded information.
- **Anti-Spam**: Implementation of the honeypot technique.

## Form Fields

- **First Name & Last Name**: Mandatory
- **Email**: Mandatory and must be valid
- **Country**: Mandatory (dropdown list)
- **Message**: Mandatory
- **Gender**: Mandatory (Radio buttons - M/F)
- **Subject**: Optional (Checkboxes - Repair, Order, Others; defaults to "Others" if none selected)

## Implementation Details

- **Server/Client Architecture**:
  - The form uses a server-client architecture where the server processes and validates the form data.
- **Sanitization**:
  - Neutralizes harmful scripts and encodings to prevent XSS attacks.
- **Validation**:
  - Ensures all mandatory fields are filled correctly and that the email address is valid.
- **Sending & Feedback**:
  - On successful validation, the user is redirected to a thank you page summarizing their input.
- **Honeypot Anti-Spam Technique**:
  - An invisible field that helps to detect and prevent spam submissions.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, jQuery
