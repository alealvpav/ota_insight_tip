from django.db import models


# All these classes should be moved to other files and modules to keep the code
# sorted and maintainable, but for now it can work.
class LogicalDeleteQueryset(models.query.QuerySet):
    """
    This is a normal Queryset but changing the behaviour of the delete method
    """
    def delete(self):
        """
        Instead of deleting from database we will hide the instances in the
        queryset, doing a "logical deletion".
        :return: Number of items affected
        :rtype: int
        """
        super(LogicalDeleteQueryset, self).delete()
        # It would be better to respect the super method return ->
        # -> (deleted_items, {object_class: deleted_items})
        return self.hide()

    def hide(self):
        """
        This method changes the field we use to logically delete elements in
        this queryset
        :return: Number of elements affected
        :rtype: int
        """
        return self.update(visible=False)


class LogicalDeleteManager(models.Manager):
    def get_query_set(self):
        return LogicalDeleteQueryset(self.model, using=self._db)


class LogicalDeleteAbstractModel(models.Model):
    visible = models.BooleanField(default=True)
    objects = LogicalDeleteManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        We are not going to allow this objects to be deleted, instead we are
        implementing a "logic deletion" function with a boolean field to avoid
        listing it (in case some day is necessary)
        :return: The instance of the Object "logically" deleted
        :rtype: Object
        """
        if self.pk:  # Only if the instance already exists in db
            self.visible = False
            self.save()
        # It would be better to respect the super method return ->
        # -> (deleted_items, {object_class: deleted_items})
        return None