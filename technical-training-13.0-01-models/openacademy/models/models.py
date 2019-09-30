from odoo import api, models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    
    name = fields.Char('Title')
    description = fields.Text('Description')
    session_ids = fields.One2many('openacademy.session', 'course_id')

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    
    name = fields.Char('Title')
    instructor_ids = fields.Many2many('openacademy.partner', string='Instructors', relation='session_partner_instructor_rel')
    course_id = fields.Many2one('openacademy.course', string='Course', required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('openacademy.partner', string='Attendees', relation='session_partner_student_rel')
    
    

class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'
    
    name = fields.Char('Name')
    type = fields.Selection([('student','Student'), ('teacher', 'Teacher')], default='student')
    