import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CustomerServiceTicketHomeComponent } from './home/CustomerServiceTicket-home.component';
import { CustomerServiceTicketNewComponent } from './new/CustomerServiceTicket-new.component';
import { CustomerServiceTicketDetailComponent } from './detail/CustomerServiceTicket-detail.component';

const routes: Routes = [
  {path: '', component: CustomerServiceTicketHomeComponent},
  { path: 'new', component: CustomerServiceTicketNewComponent },
  { path: ':id', component: CustomerServiceTicketDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CustomerServiceTicket-detail-permissions'
      }
    }
  }
];

export const CUSTOMERSERVICETICKET_MODULE_DECLARATIONS = [
    CustomerServiceTicketHomeComponent,
    CustomerServiceTicketNewComponent,
    CustomerServiceTicketDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CustomerServiceTicketRoutingModule { }