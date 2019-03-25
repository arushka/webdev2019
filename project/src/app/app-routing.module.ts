import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MenClothesComponent } from './components/men-clothes/men-clothes.component'
const routes: Routes = [
  { path: 'aru', component: MenClothesComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


