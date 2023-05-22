from datetime import date, datetime

from odoo import _, api, fields, models


class anggota_perpus (models.Model):
    _name = 'anggota.perpus'

    name = fields.Char(string="Nama")
    hp = fields.Char(string="No. Hp")
    alamat = fields.Char(string="Alamat")

class buku_perpus (models.Model):
    _name = 'buku.perpus'

    name = fields.Char(string="Judul")
    total = fields.Float(string="Total")
    deskripsi = fields.Text(string="Deskripsi")
    transaksi_perpus_ids = fields.One2many('transaksi.perpus', 'transaksi_perpus_id', string="Transaksi Perpus Ids")
    available_book =
class transaksi_perpus (models.Model):
    _name = 'transaksi.perpus'

    def _get_status(self):
        for record in self:
            if record.tanggal_selesai != False:
                if record.tanggal_selesai <= date.today():
                    record.status = 'Selesai'
                else:
                    record.status = 'On Progress'
            else:
                record.status = ''

    @api.onchange('berat')
    def func_onchange_berat(self):
            if not self.berat:
                return {}
            else:
                self.harga = self.berat * 10000

    name = fields.Char(string="Transaksi", default="New")
    tanggal_pinjam = fields.Date(string="Tanggal Pinjam")
    nama_anggota = fields.Many2one('anggota.perpus')
    judul_buku = fields.Many2one(string="buku.perpus")
    tanggal_kembali = fields.Date(string="Tanggal Kembali")
    status = fields.Char(string="Status", compute=_get_status)
    buku_perpus_id = fields.Many2one('buku.perpus', string="Buku Perpus Id")

