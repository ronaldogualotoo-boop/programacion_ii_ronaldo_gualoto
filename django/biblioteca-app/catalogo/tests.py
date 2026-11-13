<<<<<<< HEAD
from datetime import timedelta

from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from catalogo.models.autor import Autor
=======
from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

>>>>>>> main
from catalogo.models.categoria import Categoria
from catalogo.models.libro import Libro


class LoginFlowTests(TestCase):
    def test_root_redirects_to_login(self):
        response = self.client.get('/')

        self.assertRedirects(response, reverse('login'))

    def test_home_view_requires_login(self):
        response = self.client.get(reverse('home'))

        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("home")}',
        )

    def test_login_page_uses_custom_template(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/authentication/login.html')
        self.assertContains(response, 'Control de Acceso')

    def test_valid_login_redirects_to_home(self):
        User.objects.create_user(username='lector', password='clave-segura-123')

        response = self.client.post(
            reverse('login'),
            {'username': 'lector', 'password': 'clave-segura-123'},
        )

        self.assertRedirects(response, reverse('home'))

    def test_book_views_require_login(self):
        protected_urls = (
            reverse('libro_list'),
            reverse('create_libro'),
            reverse('update_libro', args=[1]),
            reverse('delete_libro', args=[1]),
        )

        for url in protected_urls:
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertRedirects(
                    response,
                    f'{reverse("login")}?next={url}',
                )

    def test_category_views_require_login(self):
        protected_urls = (
            reverse('categoria_list'),
            reverse('categoria_create'),
            reverse('categoria_update', args=[1]),
            reverse('categoria_delete', args=[1]),
        )

        for url in protected_urls:
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertRedirects(
                    response,
                    f'{reverse("login")}?next={url}',
                )

    def test_category_list_has_links_back_to_books_and_home(self):
        categoria = Categoria.objects.create(nombre='Novela')
        user = User.objects.create_user(
            username='bibliotecario',
            password='clave-segura-123',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('categoria_list'))

        self.assertContains(response, reverse('libro_list'))
        self.assertContains(response, reverse('home'))
        self.assertContains(response, 'Eliminar (sin permiso)')
        self.assertNotContains(
            response,
            reverse('categoria_delete', args=[categoria.pk]),
        )


class DeleteFlowTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Novela')
<<<<<<< HEAD
        self.autor = Autor.objects.create(nombre='Autora', apellido='Prueba')
        self.libro = Libro.objects.create(
            titulo='Libro de prueba',
=======
        self.libro = Libro.objects.create(
            titulo='Libro de prueba',
            autor='Autora',
>>>>>>> main
            fecha_publicacion='2020-01-01',
            categoria=self.categoria,
            isbn='9780000000001',
        )
<<<<<<< HEAD
        self.libro.autores.add(self.autor)
=======
>>>>>>> main
        self.book_delete_user = User.objects.create_user(
            username='bibliotecario-libros',
            password='clave-segura-123',
        )
        self.book_delete_user.user_permissions.add(Permission.objects.get(
            content_type__app_label='catalogo',
            codename='delete_libro',
        ))
        self.client.force_login(self.book_delete_user)

    def test_book_delete_confirmation_and_post(self):
        url = reverse('delete_libro', args=[self.libro.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.libro.titulo)
        self.assertContains(response, reverse('libro_list'))

        response = self.client.post(url)
        self.assertRedirects(response, reverse('libro_list'))
        self.assertFalse(Libro.objects.filter(pk=self.libro.pk).exists())

    def test_regular_user_cannot_delete_books_or_categories(self):
        self.client.logout()
        regular_user = User.objects.create_user(
            username='usuario-sin-borrado',
            password='clave-segura-123',
        )
        self.assertFalse(regular_user.is_staff)
        self.assertFalse(regular_user.is_superuser)
        self.client.force_login(regular_user)

        for url in (
            reverse('delete_libro', args=[self.libro.pk]),
            reverse('categoria_delete', args=[self.categoria.pk]),
        ):
            with self.subTest(url=url):
                response = self.client.post(url)

                self.assertEqual(response.status_code, 403)

        self.assertTrue(Libro.objects.filter(pk=self.libro.pk).exists())
        self.assertTrue(Categoria.objects.filter(pk=self.categoria.pk).exists())

    def test_category_delete_with_related_books_shows_message(self):
        category_user = User.objects.create_user(
            username='bibliotecario',
            password='clave-segura-123',
        )
        category_user.user_permissions.add(
            Permission.objects.get(
                content_type__app_label='catalogo',
                codename='delete_categoria',
            )
        )
        self.client.force_login(category_user)
        url = reverse('categoria_delete', args=[self.categoria.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.categoria.nombre)
        self.assertContains(response, reverse('categoria_list'))

        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Categoria.objects.filter(pk=self.categoria.pk).exists())
        self.assertContains(
            response,
            'No se puede eliminar la categoría porque tiene libros asociados.',
        )


class EditFlowTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre='Novela')
<<<<<<< HEAD
        self.autor = Autor.objects.create(nombre='Autora', apellido='Prueba')
        self.libro = Libro.objects.create(
            titulo='Libro de prueba',
=======
        self.libro = Libro.objects.create(
            titulo='Libro de prueba',
            autor='Autora',
>>>>>>> main
            fecha_publicacion='2020-01-01',
            categoria=self.categoria,
            isbn='9780000000001',
        )
<<<<<<< HEAD
        self.libro.autores.add(self.autor)
=======
>>>>>>> main
        self.client.force_login(
            User.objects.create_user(
                username='editor-libros',
                password='clave-segura-123',
            )
        )

    def test_book_create_saves_book(self):
        response = self.client.post(
            reverse('create_libro'),
            {
                'titulo': 'Libro nuevo',
<<<<<<< HEAD
                'autores': [self.autor.pk],
=======
                'autor': 'Autor nuevo',
>>>>>>> main
                'fecha_publicacion': '2024-01-01',
                'categoria': self.categoria.pk,
                'isbn': '9780000000002',
            },
        )

        self.assertRedirects(response, reverse('libro_list'))
        self.assertTrue(Libro.objects.filter(titulo='Libro nuevo').exists())

<<<<<<< HEAD
    def test_book_form_shows_publication_date_and_isbn_help_text(self):
        response = self.client.get(reverse('create_libro'))

        self.assertContains(response, 'La fecha de publicación no puede ser futura.')
        self.assertContains(response, 'El ISBN debe contener 13 dígitos.')

    def test_book_create_rejects_future_publication_date_and_invalid_isbn(self):
        response = self.client.post(
            reverse('create_libro'),
            {
                'titulo': 'Libro inválido',
                'autores': [self.autor.pk],
                'fecha_publicacion': (timezone.localdate() + timedelta(days=1)).isoformat(),
                'categoria': self.categoria.pk,
                'isbn': '123',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context['form'],
            'fecha_publicacion',
            'La fecha de publicación no puede ser en el futuro.',
        )
        self.assertFormError(
            response.context['form'],
            'isbn',
            'El ISBN debe tener 13 dígitos numéricos.',
        )
        self.assertFalse(Libro.objects.filter(titulo='Libro inválido').exists())

=======
>>>>>>> main
    def test_book_list_renders_when_authenticated(self):
        response = self.client.get(reverse('libro_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/libros/libro_list.html')
        self.assertContains(response, 'Eliminar (sin permiso)')
        self.assertNotContains(
            response,
            reverse('delete_libro', args=[self.libro.pk]),
        )

    def test_book_list_filters_by_search_and_category(self):
        other_category = Categoria.objects.create(nombre='Poesía')
<<<<<<< HEAD
        other_author = Autor.objects.create(nombre='Otro', apellido='Autor')
        other_book = Libro.objects.create(
            titulo='Libro de prueba alternativo',
=======
        other_book = Libro.objects.create(
            titulo='Libro de prueba alternativo',
            autor='Otro autor',
>>>>>>> main
            fecha_publicacion='2021-01-01',
            categoria=other_category,
            isbn='9780000000002',
        )
<<<<<<< HEAD
        other_book.autores.add(other_author)
=======
>>>>>>> main

        response = self.client.get(
            reverse('libro_list'),
            {'pista': 'Libro', 'categoria': self.categoria.pk},
        )

        self.assertContains(response, self.libro.titulo)
        self.assertNotContains(response, other_book.titulo)
        self.assertContains(response, self.categoria.nombre)

    def test_book_edit_updates_saved_book(self):
        url = reverse('update_libro', args=[self.libro.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Editar libro')

        response = self.client.post(
            url,
            {
                'titulo': 'Libro editado',
<<<<<<< HEAD
                'autores': [self.autor.pk],
=======
                'autor': self.libro.autor,
>>>>>>> main
                'fecha_publicacion': '2020-01-01',
                'categoria': self.categoria.pk,
                'isbn': self.libro.isbn,
            },
        )

        self.assertRedirects(response, reverse('libro_list'))
        self.libro.refresh_from_db()
        self.assertEqual(self.libro.titulo, 'Libro editado')

    def test_category_edit_updates_saved_category(self):
        User.objects.create_user(username='bibliotecario', password='clave-segura-123')
        self.client.login(username='bibliotecario', password='clave-segura-123')
        url = reverse('categoria_update', args=[self.categoria.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Editar categoría')

        response = self.client.post(
            url,
            {'nombre': 'Categoría editada', 'descripcion': 'Descripción actualizada'},
        )

        self.assertRedirects(response, reverse('categoria_list'))
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nombre, 'Categoría editada')
<<<<<<< HEAD


class AutorFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='editor-autores',
            password='clave-segura-123',
        )
        self.client.force_login(self.user)

    def test_author_create_and_list(self):
        response = self.client.post(
            reverse('autor_create'),
            {
                'nombre': 'Gabriel',
                'apellido': 'García Márquez',
                'nacionalidad': 'Colombiana',
            },
        )

        self.assertRedirects(response, reverse('autor_list'))
        autor = Autor.objects.get(nombre='Gabriel')

        response = self.client.get(reverse('autor_list'))
        self.assertTemplateUsed(response, 'catalogo/autores/autor_list.html')
        self.assertContains(response, autor.nombre)
        self.assertContains(response, autor.apellido)
        self.assertContains(response, 'Nuevo autor')

    def test_author_edit_updates_author(self):
        autor = Autor.objects.create(
            nombre='Gabriel',
            apellido='García Márquez',
            nacionalidad='Colombiana',
        )

        response = self.client.post(
            reverse('autor_update', args=[autor.pk]),
            {
                'nombre': 'Gabriel José',
                'apellido': 'García Márquez',
                'nacionalidad': 'Colombiana',
            },
        )

        self.assertRedirects(response, reverse('autor_list'))
        autor.refresh_from_db()
        self.assertEqual(autor.nombre, 'Gabriel José')

    def test_author_delete_requires_permission(self):
        autor = Autor.objects.create(nombre='Autor', apellido='De prueba')
        url = reverse('autor_delete', args=[autor.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Autor.objects.filter(pk=autor.pk).exists())

        self.user.user_permissions.add(
            Permission.objects.get(
                content_type__app_label='catalogo',
                codename='delete_autor',
            )
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, autor.nombre)

        response = self.client.post(url)
        self.assertRedirects(response, reverse('autor_list'))
        self.assertFalse(Autor.objects.filter(pk=autor.pk).exists())
=======
>>>>>>> main
