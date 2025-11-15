from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tracking_status = fields.Selection([
        ('order_date_lt', 'Order Date(Latest)'),
        ('order_date_el', 'Order Date(Earliest)'),
        ('confirmed', 'Confirmed'),
        ('received', 'Received'),
        ('receiving_error', 'Receiving Error'),
        ('ready_to_ship', 'Ready to Ship'),
        ('out_of_delivery', 'Out Of Delivery'),
        ('delivered', 'Delivered'),
        ('fulfilled', 'Fulfilled'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
        ('warranty_claim', 'Warranty Claim'),
        ('delivery_fail', 'Delivery Fail'),
        ('receive_fail', 'Receive Fail'),
        ('other', 'Other'),
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delayed', 'Delayed'),
    ], string="Order Tracking Status", default='pending',tracking=True)