from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    
    name = fields.Char('Title')
    description = fields.Text('Description')
    #session_ids = fields.One2many('openacademy.session', 'course_id')

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'
    
    name = fields.Char('Title')
    instructor_ids = fields.Many2many('openacademy.partner', string='Instructors', relation='session_partner_instructor_rel')
    course_id = fields.Many2one('openacademy.course', string='Course', required=True, ondelete='cascade')
    attendee_ids = fields.Many2many('openacademy.partner', string='Attendees', relation='session_partner_student_rel')      
    attendeetotal = fields.Float(compute='_compute_attendeetotal')
    
    @api.depends('attendee_ids')
    def _compute_attendeetotal(self):       
        for record in self:
            record.attendeetotal = len(record.attendee_ids)
            if record.attendeetotal > 2:
                raise ValidationError('Maximum attendee exceed!')
                
                

class Partner(models.Model):
    _name = 'openacademy.partner'
    _description = 'Partner'
    
    name = fields.Char('First Name') 
    lastname = fields.Char('Last Name')
    fullname = fields.Char(compute = '_compute_fullname')
    
    type = fields.Selection([('student','Student'), ('teacher', 'Teacher')], default='student')
    
    @api.depends('name', 'lastname')
    def _compute_fullname(self):
        for record in self:
            record.fullname ="%s %s" %(record.name, record.lastname)
            
    